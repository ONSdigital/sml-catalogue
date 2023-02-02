from flask import abort, escape, Markup, render_template
import markdown
from sml_builder import app


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
    return render_template("about.html", page_body=body)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


@app.route("/accessibility-statement")
def accessibility_page():
    return render_template("accessibility_statement.html")


@app.route("/.well-known/security.txt")
def security_text():
    with open(".well-known/security.txt", "r", encoding="utf-8") as input_text:
        content = input_text.read()
    return render_template("security.html", content=content)


def _page_not_found(error):
    print(error)
    abort(404)
