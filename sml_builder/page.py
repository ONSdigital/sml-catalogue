from flask import abort, render_template

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList

from .utils import _page_not_found


@app.route("/resources/about")
def about():
    # Gets the content for the about page
    content = getContent("about")
    if checkEmptyList(content):
        abort(404)
    return render_template("about.html", content=content)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    content = getContent("privacycontent")
    content["list"] = [{"text":item} for item in content["list"]]

    if checkEmptyList(content):
        abort(404)
    return render_template("content/privacy.html", content=content)


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


@app.route("/accessibility-statement")
def accessibility_page():
    content = getContent("accessibilityPage")
    if checkEmptyList(content):
        abort(404)
    return render_template("accessibility_statement.html", content=content)


@app.route("/.well-known/security.txt")
def security_text():
    try:
        with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
            content = input_text.read()
    except OSError as e:
        _page_not_found(e)
    return render_template("security.html", content=content)
