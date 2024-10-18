from json import load
from os import listdir

import pandas as pd  # pylint: disable=no-name-in-module
from flask import render_template, request

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.search_tool import search_partial
from sml_builder.utils import (
    _page_not_found,
    checkEmptyList,
    checkTypeList,
    get_feature_config,
)

method_search = get_feature_config("method_search")
search_results_info_panel = False
content_management = get_feature_config("content_management")


@app.route("/method/<methodState>/<method>")
def display_method_summary(  # pylint: disable=inconsistent-return-statements
    method, methodState
):
    if content_management["enabled"]:
        # Gets the methods for the individual method page
        getMethodsTableItems = getContent("catalogueTableOfMethods2")
        content = None
        if checkTypeList(getMethodsTableItems):
            for item in getMethodsTableItems:
                if method == item["id"]:
                    content = item
                    return render_template(
                        "method.html",
                        method=content,
                        methodState=methodState,
                        cms_enabled=content_management["enabled"],
                    )

        elif method == getMethodsTableItems["id"]:
            content = getMethodsTableItems
            return render_template(
                "method.html",
                method=content,
                methodState=methodState,
                cms_enabled=content_management["enabled"],
            )
        _page_not_found("Method summary content not found")
    else:
        with open(
            f"./content/methods/{methodState}/{method}.json", encoding="UTF-8"
        ) as json_data:
            page_data = load(json_data)
            json_data.close()
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
            return render_template(
                "method.html", page=page_data, cms_enabled=content_management["enabled"]
            )


@app.route("/methods/search", methods=["GET", "POST"])
def display_search_results():
    data = []

    if request.method == "POST":
        searchQuery = request.form["search-methods"]
    else:
        searchQuery = ""

    if content_management["enabled"]:
        content = getContent("methodsCatalogue")
        getMethodsTableItems = getContent("catalogueTableOfMethods2")
        if checkEmptyList(getMethodsTableItems) or checkEmptyList(content):
            _page_not_found("Methods content not found")
        if checkTypeList(getMethodsTableItems):
            for method in getMethodsTableItems:
                data.append(method)
        else:
            data.append(getMethodsTableItems)

        method_data = {
            "id": [item["id"] for item in data],
            "Name": [item["name"] for item in data],
            "Theme": [item["theme"] for item in data],
            "Expert Group": [item["expert_group"] for item in data],
            "Language": [item["language"] for item in data],
        }

    else:
        methods_dir = "./content/methods/ready-to-use-methods"
        future_methods_dir = "./content/methods/future-methods"

        methods = appendRow(methods_dir, filter_methods=None)
        future_methods = appendRow(future_methods_dir, filter_methods=None)

        data = methods + future_methods

        ids = [item["id"] for item in data]
        names = [item["title"] for item in data]
        themes = [item["theme"] for item in data]
        exp_groups = [item["exp_group"] for item in data]
        languages = [item["language"] for item in data]

        method_data = {
            "id": ids,
            "Name": names,
            "Theme": themes,
            "Expert Group": exp_groups,
            "Language": languages,
        }
    # Creating DataFrame
    data_frame = pd.DataFrame(method_data)

    search_results_rows = search_partial(data_frame=data_frame, query=searchQuery)
    filter_methods = search_results_rows["id"].tolist()
    try:
        # Append methods only if found in search results
        if content_management["enabled"]:
            if filter_methods is not None:
                filtered_methods = [
                    method for method in data if method["id"] in filter_methods
                ]
                methods = filtered_methods
        else:
            pass
    except OSError as e:
        _page_not_found(e)
    if content_management["enabled"]:
        return render_template(
            "methods.html",
            methods=methods,
            content=content,
            cms_enabled=content_management["enabled"],
            method_search=method_search["enabled"],
            search_results_info_panel=True,
        )
    return render_template(
        "methods.html",
        page={"rows": methods, "future_rows": None},
        query=searchQuery,
        method_search=method_search["enabled"],
        search_results_info_panel=True,
    )


@app.route("/methods/index")
def display_methods():
    if content_management["enabled"]:
        # Gets the content for the methods catalogue page
        content = getContent("methodsCatalogue")
        # Gets the methods table items for the methods catalogue page
        getMethodsTableItems = getContent("catalogueTableOfMethods2")
        if checkEmptyList(getMethodsTableItems) or checkEmptyList(content):
            _page_not_found("Methods content not found")
        methods = []
        if checkTypeList(getMethodsTableItems):
            for method in getMethodsTableItems:
                methods.append(method)
        else:
            methods.append(getMethodsTableItems)
        methods = sorted(methods, key=lambda x: x["name"])
        return render_template(
            "methods.html",
            methods=methods,
            content=content,
            cms_enabled=content_management["enabled"],
        )

    methods_dir = "./content/methods/ready-to-use-methods"
    future_methods_dir = "./content/methods/future-methods"
    try:
        methods = appendRow(methods_dir)
        future_methods = appendRow(future_methods_dir)

    except OSError as e:
        _page_not_found(e)
    return render_template(
        "methods.html",
        page={"rows": methods, "future_rows": future_methods},
        method_search=method_search["enabled"],
        search_results_info_panel=False,
        cms_enabled=content_management["enabled"],
    )


def appendRow(methods_dir, filter_methods=None):
    methods = []
    filtered_methods = []
    for file in listdir(methods_dir):
        print(file)
        with open(f"{methods_dir}/{file}", encoding="UTF-8") as json_data:
            method = load(json_data)
            json_data.close()
        methods.append(
            {
                "id": file.split(".")[0],
                "title": method["title"],
                "theme": method["method_metadata"]["Theme"],
                "exp_group": method["method_metadata"]["Expert group"],
                "language": method["method_metadata"]["Languages"],
            }
        )
    if filter_methods is not None:
        filtered_methods = [
            method for method in methods if method["id"] in filter_methods
        ]
        methods = filtered_methods
    return methods
