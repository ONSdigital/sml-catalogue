from flask import Flask, render_template, request, url_for
from flaskext.markdown import Markdown
from markupsafe import Markup, escape

from sml_builder.cms import getContent

app = Flask(__name__)
Markdown(app)

app.jinja_env.add_extension("jinja2.ext.do")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config["FREEZER_IGNORE_404_NOT_FOUND"] = True
app.config["FREEZER_DEFAULT_MIMETYPE"] = "text/html"
app.config["FREEZER_DESTINATION"] = "../build"
app.cache = {}

# F401 module import but unused
# We have to import the modules below here and they get
# used in other files later on so ignoring this F401 error
# We import the utils module and do use
# E402 module level import not at top of file
# We import the python files/ flask routes into the __init__.py file and we can't
# import them at the top of the file so ignoring them
import sml_builder.api_reference  # noqa: E402
import sml_builder.glossary  # noqa: E402
import sml_builder.help_centre  # noqa: E402
import sml_builder.method  # noqa: E402
import sml_builder.page  # noqa: E402
import sml_builder.utils  # noqa: F401, E402
from sml_builder.utils import get_feature_config  # noqa: E402
from sml_builder.utils import _page_not_found, checkEmptyList  # noqa: E402

content_management = get_feature_config("content_management")


@app.route("/")
def index():
    # Gets the content for the home page
    if content_management["enabled"]:
        content = getContent("heroHomePage")
        if checkEmptyList(content):
            _page_not_found("heroHomePage content not found")

        return render_template(
            "index.html", content=content, cms_enabled=content_management["enabled"]
        )
    return render_template("index.html", cms_enabled=content_management["enabled"])


@app.errorhandler(404)
@app.route("/page-not-found")
def page_not_found(e=None):
    return render_template("404.html"), 404 if e else 200


@app.template_filter("paras")
def string_to_paragraph(value):
    """Wraps passed string in <p> tags and converts newlines to <p> pairs"""
    body = escape(value).replace("\n\n", Markup("</p><p>"))
    return Markup(f"<p>{body}</p>")


# Method provides a dictionary to the jinja templates, allowing variables
# inside the dictionary to be directly accessed within the template files
@app.context_processor
def set_variables():
    docs_integration = sml_builder.utils.get_feature_config("docs_integration")
    navigation = {"navigation": {}}
    if docs_integration["enabled"] is True:
        nav_version = "feature_active_navigation"
        navigation["navigation"]["id"] = docs_integration["variables"][nav_version][
            "id"
        ]
        navigation["navigation"]["itemsList"] = []
        for item in docs_integration["variables"][nav_version]["itemsList"]:
            navigation["navigation"]["itemsList"].append(
                {"url": url_for(item["url"]), "title": item["title"]}
            )
        navigation["current_path"] = request.path
        return {
            "navigation": navigation,
            "docs_integration_active": docs_integration["enabled"],
        }
    return {
        "docs_integration_active": docs_integration["enabled"],
    }


# On request the method runs, pulling the help centre pages from contentful and constructs the
# navigation dictionary which creates the headers and links available on the help centre.
# On first run it removes itself from the before_request_funcs list to prevent it
# running on subsequent requests.
@app.before_request
def build_help_centre_structure():
    category_urls = {
        "Information": "information",
        "Accessing Methods": "access",
        "Feedback": "feedback",
        "Support": "support",
    }
    # Remove this method from the before_requests_funcs to prevent it from running on every user request
    app.before_request_funcs[None].remove(build_help_centre_structure)
    if content_management["enabled"]:
        nav = {"categories": []}
        contents = getContent("helpCentreInformation")
        submit_request = getContent("helpCentreMethodRequest")
        unique = set(d["help_centre_category"] for d in contents)
        for category in unique:
            nav["categories"].append(
                {
                    "name": category_urls[category],
                    "label": category,
                    "subcategories": [],
                }
            )
            for content in contents:
                if content["help_centre_category"] == category:
                    nav["categories"][-1]["subcategories"].append(
                        {"name": content["id"], "label": content["title"]}
                    )
                if not checkEmptyList(submit_request):
                    if category == "Information" and not any(
                        d["name"] == "methods-request"
                        for d in nav["categories"][-1]["subcategories"]
                    ):
                        nav["categories"][-1]["subcategories"].append(
                            {
                                "name": "methods-request",
                                "label": "Submit a method request",
                            }
                        )
        nav["categories"] = sorted(nav["categories"], key=lambda x: x["name"])
        # sort headers and links alphabetically, contentful returns content based on last updated date
        # so order would constantly change
        for category in nav["categories"]:
            category["subcategories"] = sorted(
                category["subcategories"], key=lambda x: x["label"]
            )
        app.cache["help_centre_nav"] = nav
