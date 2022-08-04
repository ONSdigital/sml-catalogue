from flask import Flask, render_template, request, g, abort, escape, Markup

app = Flask(__name__)

app.jinja_env.add_extension("jinja2.ext.do")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config["FREEZER_DEFAULT_MIMETYPE"] = "text/html"
app.config["FREEZER_DESTINATION"] = "../build"

import sml_builder.method
import sml_builder.page


@app.route("/")
def index():
    return render_template("index.html")


@app.template_filter("paras")
def string_to_paragraph(value):
    """Wraps passed string in <p> tags and converts newlines to <p> pairs"""
    body = escape(value).replace("\n", Markup("</p><p>"))
    return Markup(f"<p>{body}</p>")
