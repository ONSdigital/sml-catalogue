import os

import markdown
from flask import render_template
from markupsafe import Markup, escape

from sml_builder import app
from sml_builder.env_config import EnvConfig

from .utils import _page_not_found

environment = os.environ.get("ENV_NAME", "dev")

env_name = EnvConfig.get_environment_ga_code(environment)


@app.route("/resources/about")
def about():
    try:
        with open(
            "./content/about/about-this-library.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("about.html", page_body=body, env_name=env_name)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html", env_name=env_name)


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html", env_name=env_name)


@app.route("/accessibility-statement")
def accessibility_page():
    try:
        with open(
            "./content/accessibility/accessibility-statement.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template(
        "accessibility_statement.html", page_body=body, env_name=env_name
        )


@app.route("/.well-known/security.txt")
def security_text():
    try:
        with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
            content = input_text.read()
    except OSError as e:
        _page_not_found(e)
    return render_template("security.html", content=content, env_name=env_name)
