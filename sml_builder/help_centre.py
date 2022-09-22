from flask import abort, render_template, request, url_for, Markup, escape
from json import load
from sml_builder import app
import markdown

externallink_help_categories = [
    "report-bug",
    "provide-feedback",
    "support",
    "methods-request",
    "expert-groups",
]


@app.route("/help-centre/index")
def help_centre(category=None):
    categories = []
    with open("./content/help_centre/help_centre.json") as help_contents_file:
        contents = load(help_contents_file)
    for category in contents["categories"]:
        categories.append(
            {
                "name": category["label"],
                "subcategories": [
                    {
                        "url": url_for(
                            "guidances",
                            category=category["name"],
                            sub_category=sub_category["name"],
                        ),
                        "text": sub_category["label"],
                    }
                    for sub_category in category["subcategories"]
                ],
            }
        )

    return render_template(
        "help.html", help_categories=categories, selected_category=category
    )


@app.route("/help-centre/<category>/index")
@app.route("/help-centre/<category>/<sub_category>")
def guidances(category, sub_category=None):
    try:
        category_label, sub_category_label, sub_category = _get_category_labels(
            category, sub_category
        )
    except Exception as e:
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
        body = Markup(markdown.markdown(text))
    else:
        if sub_category in ["methods-request", "expert-groups"]:
            body = sub_category
        else:
            body = False

    help_centre_nav = _help_centre_nav(category)

    return render_template(
        "help_category.html",
        body=body,
        category_label=category_label,
        sub_category_label=sub_category_label,
        category=category,
        sub_category=sub_category,
        nav=help_centre_nav,
    )


def _get_category_labels(selected_category, selected_sub_category):
    with open("./content/help_centre/help_centre.json") as help_contents_file:
        contents = load(help_contents_file)
    for category in contents["categories"]:
        if category["name"] == selected_category:
            category_label = category["label"]
            if selected_sub_category == None:
                return (
                    category_label,
                    category["subcategories"][0]["label"],
                    category["subcategories"][0]["name"],
                )
            for sub_category in category["subcategories"]:
                if sub_category["name"] == selected_sub_category:
                    sub_category_label = sub_category["label"]
                    return category_label, sub_category_label, selected_sub_category
            raise Exception(
                f"The sub category {selected_sub_category} was not found in the category '{selected_category}'"
            )
    raise Exception(f"The category '{selected_category}' was not found")


def _help_centre_nav(
    current_category,
):
    with open("./content/help_centre/help_centre.json") as help_contents_file:
        contents = load(help_contents_file)
    return [
        {
            "title": category["label"],
            "url": url_for(
                "guidances",
                category=category["name"],
            ),
            "anchors": [
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
            else None,
        }
        for category in contents["categories"]
    ]


def _page_not_found(error):
    print(error)
    abort(404)
