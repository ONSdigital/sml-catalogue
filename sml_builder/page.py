import markdown
from flask import abort, render_template
from markupsafe import Markup, escape

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList
from sml_builder.utils import get_feature_config

from .utils import _page_not_found


cms_enabled = get_feature_config("CONTENT_MANAGEMENT_SYSTEM")

@app.route("/resources/about")
def about():
    # Gets the content for the about page
    if cms_enabled:
        content = getContent("about")
        if checkEmptyList(content):
            abort(404)
        return render_template("about.html", content=content, cms_enabled=cms_enabled)
    
    try:
        with open(
            "./content/about/about-this-library.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("about.html", page_body=body, cms_enabled=cms_enabled)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    if cms_enabled:
        content = getContent("privacycontent")
        content["bullet_list"] = [{"text": item} for item in content["bullet_list"]]

        if checkEmptyList(content):
            abort(404)
        return render_template("content/privacy.html", content=content, cms_enabled=cms_enabled)
    return render_template("content/privacy.html", cms_enabled=cms_enabled)


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


@app.route("/accessibility-statement")
def accessibility_page():
    if cms_enabled:
        content = getContent("accessibilityPage")
        if checkEmptyList(content):
            abort(404)
        return render_template("accessibility_statement.html", content=content, cms_enabled=cms_enabled)
    
    try:
        with open(
            "./content/accessibility/accessibility-statement.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("accessibility_statement.html", page_body=body, cms_enabled=cms_enabled)


@app.route("/.well-known/security.txt")
def security_text():
    try:
        with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
            content = input_text.read()
    except OSError as e:
        _page_not_found(e)
    return render_template("security.html", content=content)
