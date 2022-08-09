from os import listdir
from flask import request, render_template, redirect, url_for, abort, g
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app


@app.route("/method/<method>")
def display_method(method):
    return render_template(
        "method.html", page=loads(evaluate_file(f"./content/methods/{method}.jsonnet"))
    )


@app.route("/methods")
def display_methods():
    methods = []
    methods_dir = "./content/methods"
    for file in listdir(methods_dir):
        method = loads(evaluate_file(f"{methods_dir}/{file}"))
        methods.append(
            {
                "tds": [
                    {
                        "value": f'<a href="{url_for("display_method", method=file.split(".")[0])}">{method["title"]}</a>'
                    },
                    {"value": method["method_metadata"]["Theme"]},
                    {"value": method["method_metadata"]["Expert group"]},
                    {"value": method["method_metadata"]["Programming language"]},
                    {"value": method["method_metadata"]["Access type"]},
                    {"value": method["method_metadata"]["Status"]},
                ]
            }
        )
    return render_template("methods.html", page={"rows": methods})


@app.route("/help-centre")
def help_centre():
    return render_template("help-centre.html")


@app.route("/help-centre/<category>/<sub_category>")
def guidance(category=None, sub_category=None):
    guidances = []
    categories = []
    methods_dir = "./content/help_centre"
    guidances_content = loads(evaluate_file(f"{methods_dir}/{sub_category}.jsonnet"))
    for guide in guidances_content["guidances"]:
        guidances.append({"text": guide})
    for category in guidances_content["categories"]:
        categories.append(
            {"title": "Section 1", "url": "#section-1"},
        )
    return render_template(
        "guidance-category.html",
        data={
            "overview_text": guidances_content["header3"],
            "guidances": guidances,
            "current_path": request.base_url,
        },
    )
