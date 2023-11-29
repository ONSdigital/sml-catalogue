from json import load

from flask import render_template, url_for

from sml_builder import app

from .utils import _page_not_found


@app.route("/api_reference/index")
def api_reference(category=None):
    categories = []
    try:
        with open(
            "./content/api_reference/api_reference.json", encoding="utf-8"
        ) as help_contents_file:
            contents = load(help_contents_file)
        for category in contents[  # pylint: disable=redefined-argument-from-local
            "categories"
        ]:
            categories.append(
                {
                    "name": category["label"],
                    "subcategories": [
                        {
                            "url": url_for(
                                "api_guidances",
                                category=category["name"],
                                sub_category=sub_category["name"],
                            ),
                            "text": sub_category["label"],
                        }
                        for sub_category in category["subcategories"]
                    ],
                }
            )
    except OSError as e:
        _page_not_found(e)
    return render_template(
        "api-index.html", help_categories=categories, selected_category=category
    )


@app.route("/api_reference/<category>/index")
@app.route("/api_reference/<category>/<sub_category>")
def api_guidances(category, sub_category=None):
    try:
        category_label, sub_category_label, sub_category = _get_category_labels(
            category, sub_category
        )
    except Exception as e:  # pylint: disable=broad-except
        _page_not_found(e)

    api_reference_nav = _api_reference_nav(category)

    return render_template(
        "api-reference.html",
        category_label=category_label,
        sub_category_label=sub_category_label,
        category=category,
        sub_category=sub_category,
        nav=api_reference_nav,
    )


def _get_category_labels(selected_category, selected_sub_category):
    with open(
        "./content/api_reference/api_reference.json", encoding="utf-8"
    ) as help_contents_file:
        contents = load(help_contents_file)
    for category in contents["categories"]:
        if category["name"] == selected_category:
            category_label = category["label"]
            if selected_sub_category is None:
                return (
                    category_label,
                    category["subcategories"][0]["label"],
                    category["subcategories"][0]["name"],
                )
            for sub_category in category["subcategories"]:
                if sub_category["name"] == selected_sub_category:
                    sub_category_label = sub_category["label"]
                    return category_label, sub_category_label, selected_sub_category
            raise KeyError(
                f"The sub category {selected_sub_category} was not found in the category '{selected_category}'"
            )
    raise KeyError(f"The category '{selected_category}' was not found")


def _api_reference_nav(
    current_category,
):
    with open(
        "./content/api_reference/api_reference.json", encoding="utf-8"
    ) as help_contents_file:
        contents = load(help_contents_file)
    return [
        {
            "title": category["label"],
            "anchors": [
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
            else None,
        }
        for category in contents["categories"]
    ]
