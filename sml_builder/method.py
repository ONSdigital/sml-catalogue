from os import listdir
from flask import render_template, url_for, abort
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app
from sml_builder.cms import getContent

STATUS_CLASS = {
    "In development": "pending",
    "Complete": "success",
    "Approved for development": "dead",
}


@app.route("/method/<method>")
def display_method(method):
    # Gets the methods for the individual method page
    getMethodsTableItems = getContent("catalogueTableOfMethods2")
    content = None

    for item in getMethodsTableItems:
        if method == item["id"]:
            content = item
            return render_template("method.html", method=content, status_class=STATUS_CLASS)

    if content is None:
        abort(404)


@app.route("/methods")
def display_methods():
    # Gets the content for the methods catalogue page
    content = getContent("methodsCatalogue")
    # Gets the methods table items for the methods catalogue page
    getMethodsTableItems = getContent("catalogueTableOfMethods2")

    methods = []
    for method in getMethodsTableItems:
        methods.append(method)

    return render_template(
        "methods.html", methods=methods, status_class=STATUS_CLASS, content=content
    )