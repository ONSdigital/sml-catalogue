from flask import abort, render_template

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList, checkTypeList

STATUS_CLASS = {
    False: "pending",
    True: "success",
}


@app.route("/method/<method>")
def display_method(method):  # pylint: disable=inconsistent-return-statements
    # Gets the methods for the individual method page
    getMethodsTableItems = getContent("catalogueTableOfMethods2")

    content = None

    if checkTypeList(getMethodsTableItems):
        for item in getMethodsTableItems:
            if method == item["id"]:
                content = item
                return render_template(
                    "method.html", method=content, status_class=STATUS_CLASS
                )

    elif method == getMethodsTableItems["id"]:
        content = getMethodsTableItems
        return render_template("method.html", method=content, status_class=STATUS_CLASS)
    abort(404)


@app.route("/methods")
def display_methods():
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
        "methods.html", methods=methods, status_class=STATUS_CLASS, content=content
    )
