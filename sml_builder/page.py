from flask import abort, render_template
from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList
from flask import escape, Markup, render_template
import markdown
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
    return render_template("content/privacy.html")


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


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
    return render_template("accessibility_statement.html", page_body=body)


@app.route("/.well-known/security.txt")
def security_text():
    try:
        with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
            content = input_text.read()
    except OSError as e:
        _page_not_found(e)
    return render_template("security.html", content=content)
