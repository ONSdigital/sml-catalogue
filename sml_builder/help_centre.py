from flask import abort, render_template, request, url_for, Markup, escape
from json import load
from sml_builder import app
import markdown
from os import listdir


@app.route("/help")
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
                            expanded_category=category["name"],
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


@app.route("/help/<category>/<sub_category>")
def guidances(category, sub_category):

    try:
        category_label, sub_category_label = _get_category_labels(
            category, sub_category
        )
    except Exception as e:
        _page_not_found(e)

    try:
        with open(
            f"./content/help_centre/{sub_category}.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
    except OSError as e:
        _page_not_found(e)
    escaped_text = escape(text)
    print(markdown.markdown(escaped_text))
    body = Markup(markdown.markdown(escaped_text))

    expanded_category = request.args.get("expanded_category", category)
    help_centre_nav = _help_centre_nav(expanded_category, category, sub_category)

    return render_template(
        "help_category.html",
        body=body,
        category_label=category_label,
        sub_category_label=sub_category_label,
        category=category,
        sub_category=sub_category,
        nav=help_centre_nav,
    )
    guidances_content = loads(evaluate_file("./content/help_centre/guidances.jsonnet"))
    instructions = []
    for guidance in guidances_content[sub_category]["guidances"]:
        guidance_items = []
        for detail in guidance["details"]:
            hyperlink_text = detail
            if guidance["hyper_link"]:
                for key, value in guidance["hyper_link"].items():
                    hyperlink_text = re.sub(
                        key,
                        f"<a href='{value}' >{key}</a>",
                        detail,
                    )
            guidance_items.append({"text": hyperlink_text})
        instructions.append(
            (
                guidance["description"],
                guidance_items,
            )
        )
    categories = []
    help_content = loads(evaluate_file("./content/help_centre/help_centre.libsonnet"))
    for category in help_content["categories"]:
        current = "#0"
        category_anchors = []
        for sub_cat in category["subcategories"]:
            path = url_for("guidances", sub_category=sub_cat["name"])
            category_anchors.append(
                {
                    "url": path,
                    "title": sub_cat["label"],
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


def _get_category_labels(selected_category, selected_sub_category):
    with open("./content/help_centre/help_centre.json") as help_contents_file:
        contents = load(help_contents_file)
    for category in contents["categories"]:
        if category["name"] == selected_category:
            category_label = category["label"]
            for sub_category in category["subcategories"]:
                if sub_category["name"] == selected_sub_category:
                    sub_category_label = sub_category["label"]
                    return category_label, sub_category_label
            raise Exception(
                f"The sub category {selected_sub_category} was not found in the category '{selected_category}'"
            )
    raise Exception(f"The category '{selected_category}' was not found")


def _help_centre_nav(
    expanded_category,
    current_category,
    current_subcategory,
):
    with open("./content/help_centre/help_centre.json") as help_contents_file:
        contents = load(help_contents_file)
    return [
        {
            "title": category["label"],
            "url": url_for(
                "guidances",
                category=current_category,
                sub_category=current_subcategory,
                expanded_category=category["name"],
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
            if category["name"] == expanded_category
            else None,
        }
        for category in contents["categories"]
    ]


def _page_not_found(error):
    print(error)
    abort(404)
