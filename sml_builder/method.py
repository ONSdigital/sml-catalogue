import pandas as pd
from json import loads
from os import listdir

from _jsonnet import evaluate_file  # pylint: disable=no-name-in-module
from flask import render_template, request

from sml_builder import app

from .utils import _page_not_found, get_feature_config

from .search_tool import search_partial

search_feature = get_feature_config("search_feature")

@app.route("/method/<methodState>/<method>")
def display_method_summary(method, methodState):
    page_data = loads(
        evaluate_file(f"./content/methods/{methodState}/{method}.jsonnet")
    )
    # Manually sorting the order of the method_metadata dictionary, the jsonnet library automatically sorts the
    # resulting dictionary and nested dictionaries alphabetically, this lets us select the desired order when using the
    # onsMetadata component

    sorted_order = [
        "Author",
        "Theme",
        "Expert group",
        "Languages",
        "Release",
    ]
    page_data["method_metadata"] = {
        k: page_data["method_metadata"][k] for k in sorted_order
    }
    return render_template("method.html", page=page_data)

@app.route("/methods/search/", methods=['POST'])
def display_search_results():
    data = []
    searchQuery = request.form['search-methods']

    methods_dir = "./content/methods/ready-to-use-methods"
    future_methods_dir = "./content/methods/future-methods"

    # Display results
    methods = appendRow(methods_dir, filter=None)
    future_methods = appendRow(future_methods_dir, filter=None)

    data = methods + future_methods

    ids = [item['id'] for item in data]
    names = [item['title'] for item in data]
    themes = [item['theme'] for item in data]
    exp_groups = [item['exp_group'] for item in data]
    languages = [item['language'] for item in data]

    method_data = {
            "id" : ids,
            "Name" : names,
            "Theme" : themes,
            "Expert Group" : exp_groups,
            "Language" : languages,
    }

    # Creating DataFrame
    data_frame = pd.DataFrame(method_data)

    search_results_rows = search_partial(data_frame=data_frame, query=searchQuery)
    filter = search_results_rows["id"].tolist()
    try:
        # append methods only if found in search results
        methods = appendRow(methods_dir, filter=filter)
        future_methods = appendRow(future_methods_dir, filter=filter)
    except OSError as e:
        _page_not_found(e)
    return render_template(
        "methods.html", page={"rows": methods, "future_rows":future_methods}, query=searchQuery, search_details_open=True, search_feature=search_feature["enabled"]
    )

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
        "methods.html", page={"rows": methods, "future_rows": future_methods}, search=False, search_details_open=False, search_feature=search_feature["enabled"]
    )


def appendRow(methods_dir, filter=None):
    methods = []
    filtered_methods = []
    for file in listdir(methods_dir):
        method = loads(evaluate_file(f"{methods_dir}/{file}"))

        methods.append(
            {
                "id": file.split(".")[0],
                "title": method["title"],
                "theme": method["method_metadata"]["Theme"],
                "exp_group": method["method_metadata"]["Expert group"],
                "language": method["method_metadata"]["Languages"],
            }
        )
    if filter is not None:
        filtered_methods = [method for method in methods if method["id"] in filter]
        methods = filtered_methods
    return methods
