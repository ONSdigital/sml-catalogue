from os import listdir
from flask import render_template, url_for
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
    page_data = loads(evaluate_file(f"./content/methods/{method}.jsonnet"))
    return render_template("method.html", page=page_data, status_class=STATUS_CLASS)


@app.route("/methods")
def display_methods():
    content = getContent("methodsCatalogue")
    methods = []
    methods_dir = "./content/methods"
    for file in listdir(methods_dir):
        method = loads(evaluate_file(f"{methods_dir}/{file}"))

        methods.append(
            {
                "id": file.split(".")[0],
                "title": method["title"],
                "theme": method["method_metadata"]["Theme"],
                "exp_group": method["method_metadata"]["Expert group"],
                "language": method["method_metadata"]["Programming language"],
                "access": method["method_metadata"]["Access type"],
                "status": method["method_metadata"]["Status"],
            }
        )
    return render_template(
        "methods.html", page={"rows": methods}, status_class=STATUS_CLASS, content=content
    )