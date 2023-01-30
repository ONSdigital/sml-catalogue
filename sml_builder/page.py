from flask import abort, render_template
from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList


@app.route("/resources/about")
def about():
    # Gets the content for the about page
    content = getContent("about")
    if checkEmptyList(content):
        abort(404)
    return render_template("about.html", content=content)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


@app.route("/.well-known/security.txt")
def security_text():
    with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
        content = input_text.read()
    return render_template("security.html", content=content)


def _page_not_found(error):
    print(error)
    abort(404)
