from os import listdir
from flask import render_template, url_for, abort
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app
from sml_builder.headlessCMS import getContent

STATUS_CLASS = {
    "In development": "pending",
    "Complete": "success",
    "Approved for development": "dead",
}


@app.route("/method/<method>")
def display_method(method):
    getContentMethodsTable = getContent("catalogueTableOfMethods2", True)
    content = None
    # print(getContentMethodsTable)
    for item in getContentMethodsTable:
        if method == item["id"]:
            content = item
            return render_template("method.html", method=content, status_class=STATUS_CLASS)

    if content is None:
        abort(404)


@app.route("/methods")
def display_methods():
    content = getContent("methodsCatalogue", False)
    getContentMethodsTable = getContent("catalogueTableOfMethods2", True)
    methods = []
    for method in getContentMethodsTable:
        methods.append(method)
    return render_template(
        "methods.html", methods=methods, status_class=STATUS_CLASS, content=content
    )