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
    # print("Output", getContentMethodsTable)
    methods = []
    for method in getContentMethodsTable:
        # print(method)
        methods.append(method)
    # methods_dir = "./content/methods"
    # for file in listdir(methods_dir):
    #     method = loads(evaluate_file(f"{methods_dir}/{file}"))

    #     methods.append(
    #         {
    #             "id": file.split(".")[0],
    #             "title": method["title"],
    #             "theme": method["method_metadata"]["Theme"],
    #             "exp_group": method["method_metadata"]["Expert group"],
    #             "language": method["method_metadata"]["Programming language"],
    #             "access": method["method_metadata"]["Access type"],
    #             "status": method["method_metadata"]["Status"],
    #         }
    #     )

    # print(methods)
    return render_template(
        "methods.html", methods=methods, status_class=STATUS_CLASS, content=content
    )