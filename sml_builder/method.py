from os import listdir
from json import loads
from flask import render_template
from _jsonnet import evaluate_file  # pylint: disable=no-name-in-module
from sml_builder import app
from .utils import _page_not_found


@app.route("/method/<method>")
def display_method(method):
    page_data = loads(
        evaluate_file(f"./content/methods/{methodState}/{method}.jsonnet")
    )
    return render_template("method.html", page=page_data)


@app.route("/method/<methodState>/<method>")
def display_method_summary(method, methodState):
    page_data = loads(evaluate_file(f"./content/methods/{methodState}/{method}.jsonnet"))
    return render_template("method.html", page=page_data)


@app.route("/methods")
def display_methods():
    methods_dir = "./content/methods/ready-to-use-methods"
    future_methods_dir = "./content/methods/future-methods"
    try:

        methods = appendRow(methods_dir)
        future_methods = appendRow(future_methods_dir)

    except OSError as e:
        _page_not_found(e)
    return render_template(
        "methods.html", page={"rows": methods, "future_rows": future_methods}
    )


def appendRow(methods_dir):
    methods = []
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
            }
        )
    return methods
