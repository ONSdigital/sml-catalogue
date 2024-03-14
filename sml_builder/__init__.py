from flask import Flask, render_template, request, url_for
from markupsafe import Markup, escape

app = Flask(__name__)

app.jinja_env.add_extension("jinja2.ext.do")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config["FREEZER_DEFAULT_MIMETYPE"] = "text/html"
app.config["FREEZER_DESTINATION"] = "../build"

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


@app.route("/")
def index():
    return render_template("index.html")


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
    if docs_integration["enabled"] is False:
        nav_version = "feature_disabled_navigation"
    else:
        nav_version = "feature_active_navigation"
    navigation["navigation"]["id"] = docs_integration["variables"][nav_version]["id"]
    navigation["navigation"]["itemsList"] = []
    for item in docs_integration["variables"][nav_version]["itemsList"]:
        navigation["navigation"]["itemsList"].append(
            {"url": url_for(item["url"]), "title": item["title"]}
        )
    navigation["current_path"] = request.path
    return {"navigation": navigation, "docs_integration_active": docs_integration["enabled"]}
