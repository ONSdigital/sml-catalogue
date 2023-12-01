import os

from flask import Flask, render_template
from markupsafe import Markup, escape

from sml_builder.env_config import EnvConfig

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
import sml_builder.glossary  # noqa: E402
import sml_builder.help_centre  # noqa: E402
import sml_builder.method  # noqa: E402
import sml_builder.page  # noqa: E402
import sml_builder.utils  # noqa: F401, E402

environment = os.environ.get("ENV_NAME", "dev")

env_name = EnvConfig.get_environment_ga_code(environment)


@app.route("/")
def index():
    return render_template("index.html", env_name=env_name)


@app.errorhandler(404)
@app.route("/page-not-found")
def page_not_found(e=None):
    return render_template("404.html", env_name=env_name), 404 if e else 200


@app.template_filter("paras")
def string_to_paragraph(value):
    """Wraps passed string in <p> tags and converts newlines to <p> pairs"""
    body = escape(value).replace("\n\n", Markup("</p><p>"))
    return Markup(f"<p>{body}</p>")
