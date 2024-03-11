from flask import abort, render_template
from json import loads
from os import listdir

from _jsonnet import evaluate_file #pylint: disable=no-name-in-module
from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList, checkTypeList, _page_not_found, get_feature_config

cms_enabled = get_feature_config("CONTENT_MANAGEMENT_SYSTEM")


@app.route("/method/<methodState>/<method>")
def display_method_summary(method, methodState):  # pylint: disable=inconsistent-return-statements
    if cms_enabled:
        # Gets the methods for the individual method page
        getMethodsTableItems = getContent("catalogueTableOfMethods2")
        content = None
        if checkTypeList(getMethodsTableItems):
            for item in getMethodsTableItems:
                if method == item["id"]:
                    content = item
                    return render_template(
                        "method.html", method=content, methodState=methodState
                    )

        elif method == getMethodsTableItems["id"]:
            content = getMethodsTableItems
            return render_template("method.html", method=content, methodState=methodState)
        abort(404) 
    else:
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


@app.route("/methods")
def display_methods():
    if cms_enabled:
        # Gets the content for the methods catalogue page
        content = getContent("methodsCatalogue")
        # Gets the methods table items for the methods catalogue page
        getMethodsTableItems = getContent("catalogueTableOfMethods2")
        if checkEmptyList(getMethodsTableItems) or checkEmptyList(content):
            abort(404)
        methods = []
        if checkTypeList(getMethodsTableItems):
            for method in getMethodsTableItems:
                methods.append(method)
        else:
            methods.append(getMethodsTableItems)
        return render_template(
            "methods.html", methods=methods, content=content
        )
    else:
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
                "language": method["method_metadata"]["Languages"],
            }
        )
    return methods