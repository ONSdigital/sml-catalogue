from json import load

import markdown
from flask import render_template, url_for
from markupsafe import Markup, escape

from sml_builder import app

from .utils import _page_not_found, category_labels, contents_helper

externallink_help_categories = [
    "report-bug",
    "provide-feedback",
    "support",
    "methods-request",
    "expert-groups",
]


@app.route("/help-centre/index")
def help_centre(category=None):
    try:
        with open(
            "./content/help_centre/help_centre.json", encoding="utf-8"
        ) as help_contents_file:
            contents = load(help_contents_file)
            categories = contents_helper(contents, "guidances")

    except OSError as e:
        _page_not_found(e)
    return render_template(
        "help.html", help_categories=categories, selected_category=category
    )


@app.route("/help-centre/<category>/index")
@app.route("/help-centre/<category>/<sub_category>")
def guidances(category, sub_category=None):
    try:
        category_label, sub_category_label, sub_category = category_labels(
            "./content/help_centre/help_centre.json", category, sub_category
        )
    except Exception as e:  # pylint: disable=broad-except
        _page_not_found(e)

    if sub_category not in externallink_help_categories:
        try:
            with open(
                f"./content/help_centre/{sub_category}.md", "r", encoding="utf-8"
            ) as input_file:
                text = input_file.read()
        except OSError as e:
            _page_not_found(e)
        escaped_text = escape(text)
        body = Markup(markdown.markdown(escaped_text))
    else:
        body = False

    help_centre_nav = _help_centre_nav(category)

    return render_template(
        (
            "help-methods-request.html"
            if sub_category == "methods-request"
            else "help_category.html"
        ),
        body=body,
        category_label=category_label,
        sub_category_label=sub_category_label,
        category=category,
        sub_category=sub_category,
        nav=help_centre_nav,
    )


def _help_centre_nav(
    current_category,
):
    with open(
        "./content/help_centre/help_centre.json", encoding="utf-8"
    ) as help_contents_file:
        contents = load(help_contents_file)
    return [
        {
            "title": "Other 'how to' list categories",
            "itemsList": [
                {
                    "title": category["label"],
                    "url": url_for(
                        "guidances",
                        category=category["name"],
                    ),
                    "anchors": (
                        [
                            {
                                "title": sub_category["label"],
                                "url": url_for(
                                    "guidances",
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
