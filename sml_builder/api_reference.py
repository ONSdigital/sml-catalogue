from json import load

from flask import Response, render_template, url_for

from sml_builder import app
from sml_builder.utils import (
    _page_not_found,
    category_labels,
    contents_helper,
    get_feature_config,
)


@app.route("/api_reference/index")
def api_reference(category=None):
    mkdocs = get_feature_config("docs_integration")
    if mkdocs["enabled"] is True:
        try:
            with open(
                "./content/api_reference/api_reference.json", encoding="utf-8"
            ) as help_contents_file:
                contents = load(help_contents_file)
                categories = contents_helper(contents, "api_guidances")
                print(categories)
        except OSError as e:
            _page_not_found(e)
        return render_template(
            "api-index.html", help_categories=categories, selected_category=category
        )
    return Response("Feature is a work in progress")


@app.route("/api_reference/<category>/index")
@app.route("/api_reference/<category>/<sub_category>")
def api_guidances(category, sub_category=None):
    mkdocs = get_feature_config("docs_integration")
    if mkdocs["enabled"] is True:
        try:
            with open(
                "./content/api_reference/api_reference.json", encoding="utf-8"
            ) as help_contents_file:
                contents = load(help_contents_file)
            category_label, sub_category_label, sub_category = category_labels(
                contents, category, sub_category
            )
        except Exception as e:  # pylint: disable=broad-except
            _page_not_found(e)

        api_reference_nav = _api_reference_nav(category)
        body = f"api-docs/{category}/{sub_category}/{sub_category}.html"
        return render_template(
            "api-reference.html",
            body=body,
            category_label=category_label,
            sub_category_label=sub_category_label,
            category=category,
            sub_category=sub_category,
            nav=api_reference_nav,
        )
    return Response("Feature is a work in progress")


# Converts json file, converting url fields into Flask URL objects and arranging
# fields into appropriate structure for ONS Design System
def _api_reference_nav(
    current_category,
):
    with open(
        "./content/api_reference/api_reference.json", encoding="utf-8"
    ) as help_contents_file:
        contents = load(help_contents_file)
    return [
        {
            "title": "API Reference",
            "itemsList": [
                {
                    "title": category["label"],
                    "url": url_for(
                        "api_guidances",
                        category=category["name"],
                    ),
                    "anchors": (
                        [
                            {
                                "title": sub_category["label"],
                                "url": url_for(
                                    "api_guidances",
                                    category=category["name"],
                                    sub_category=sub_category["name"],
                                ),
                            }
                            for sub_category in category["subcategories"]
                        ]
                        if category["name"] == current_category
                        else None
                    ),
                }
                for category in contents["categories"]
            ],
        }
    ]
