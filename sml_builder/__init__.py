from flask import Flask, abort, render_template
from flaskext.markdown import Markdown
from markupsafe import Markup, escape

from sml_builder.cms import getContent

app = Flask(__name__)
Markdown(app)

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
import sml_builder.glossary  # noqa: E402
import sml_builder.help_centre  # noqa: E402
import sml_builder.method  # noqa: E402
import sml_builder.page  # noqa: E402
import sml_builder.utils  # noqa: F401, E402
from sml_builder.utils import checkEmptyList  # noqa: E402
from sml_builder.utils import get_feature_config  # noqa: E402

cms_enabled = get_feature_config("CONTENT_MANAGEMENT_SYSTEM")


@app.route("/")
def index():
    # Gets the content for the home page
    if cms_enabled:
        content = getContent("heroHomePage")
        if checkEmptyList(content):
            abort(404)

        return render_template("index.html", content=content, cms_enabled=cms_enabled)
    return render_template("index.html", cms_enabled=cms_enabled)


@app.errorhandler(404)
@app.route("/page-not-found")
def page_not_found(e=None):
    return render_template("404.html"), 404 if e else 200


@app.template_filter("paras")
def string_to_paragraph(value):
    """Wraps passed string in <p> tags and converts newlines to <p> pairs"""
    body = escape(value).replace("\n\n", Markup("</p><p>"))
    return Markup(f"<p>{body}</p>")
