from flask import abort, render_template
from sml_builder import app
from sml_builder.headlessCMS import getContent


@app.route("/resources/about")
def about():
    content = getContent("about", False)
    return render_template("about.html", content=content)


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


def _page_not_found(error):
    print(error)
    abort(404)
