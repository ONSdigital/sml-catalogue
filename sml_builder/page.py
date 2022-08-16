from flask import render_template
from sml_builder import app


@app.route("/help")
def help():
    return "help"


@app.route("/resources/about")
def resources():
    return render_template("about.html")


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")
