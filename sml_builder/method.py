from flask import request, render_template, redirect, url_for, abort, g
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app


@app.route("/method/<method>")
def display_method(method):
    return render_template(
        "method.html", page=loads(evaluate_file(f"./content/methods/{method}.jsonnet"))
    )
