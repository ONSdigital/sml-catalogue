from flask import render_template, request, url_for
from sml_builder import app
from json import loads
from _jsonnet import evaluate_file


@app.route("/help")
def help_centre():
    categories = []
    content = loads(evaluate_file("./content/help_centre/help_centre.libsonnet"))
    for category in content["categories"]:
        categories.append(
            {
                "name": category["label"],
                "subcategories": [
                    {
                        "url": url_for("guidances", sub_category=sub_category["name"]),
                        "text": sub_category["label"],
                    }
                    for sub_category in category["subcategories"]
                ],
            }
        )

    return render_template("help.html", help_categories=categories)


@app.route("/help/<sub_category>")
def guidances(sub_category=None):
    guidances_content = loads(evaluate_file("./content/help_centre/guidances.jsonnet"))
    instructions = []
    for guidance in guidances_content[sub_category]["guidances"]:
        instructions.append(
            (
                guidance["description"],
                [{"text": detail} for detail in guidance["details"]],
            )
        )
    categories = []

    help_content = loads(evaluate_file("./content/help_centre/help_centre.libsonnet"))
    for category in help_content["categories"]:
        current = "#0"
        category_anchors = []
        for sub in category["subcategories"]:
            path = url_for("guidances", sub_category=sub["name"])
            category_anchors.append(
                {
                    "url": path,
                    "title": sub["label"],
                }
            )
            if path == request.path:
                current = path

        categories.append(
            {
                "title": category["label"],
                "url": current,
                "anchors": category_anchors,
            }
        )
    return render_template(
        "guidances.html",
        data={
            "overview_text": guidances_content[sub_category]["header3"],
            "guidances_content": instructions,
            "current_path": request.path,
            "categories": categories,
        },
    )


@app.route("/resources")
def resources():
    return render_template("about.html")


@app.route("/privacy-and-data-protection")
def privacy_and_data_protection():
    return render_template("content/privacy.html")
