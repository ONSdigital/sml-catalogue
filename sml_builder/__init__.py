import re
from flask import Flask, render_template, request, g, abort, escape, Markup

app = Flask(__name__)

app.jinja_env.add_extension("jinja2.ext.do") # pylint: disable=no-member
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config["FREEZER_DEFAULT_MIMETYPE"] = "text/html"
app.config["FREEZER_DESTINATION"] = "../build"

import sml_builder.method
import sml_builder.page
import sml_builder.glossary
import sml_builder.utils
import sml_builder.help_centre


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
