from flask import render_template, request, url_for
from sml_builder import app
from json import loads
from _jsonnet import evaluate_file
import re


@app.route("/resources/about")
def about():
    return render_template("about.html")


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")
