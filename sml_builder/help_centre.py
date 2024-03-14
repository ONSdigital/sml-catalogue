from json import load

import markdown
from flask import abort, render_template, url_for
from markupsafe import Markup, escape

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList, get_feature_config

from .utils import _page_not_found

externallink_help_categories = [
    "report-bug",
    "provide-feedback",
    "support",
    "methods-request",
    "expert-groups",
]

cms_enabled = get_feature_config("CONTENT_MANAGEMENT_SYSTEM")


@app.route("/help-centre/index")
def help_centre(category=None):
    categories = []
    try:
        if cms_enabled:
            contents = getContent("helpCentreStructure")["structure"]
            if checkEmptyList(contents):
                abort(404)
        else:
            with open(
                "./content/help_centre/help_centre.json", encoding="utf-8"
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
    except OSError as e:
        _page_not_found(e)
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
    except Exception as e:  # pylint: disable=broad-except
        _page_not_found(e)
    help_centre_nav = _help_centre_nav(category)

    if cms_enabled:
        if sub_category == "methods-request":
            content = getContent("helpCentreMethodRequest")
            if checkEmptyList(content):
                abort(404)
            return render_template(
                "help-methods-request.html",
                body=content,
                category_label=category_label,
                sub_category_label=sub_category_label,
                category=category,
                sub_category=sub_category,
                nav=help_centre_nav,
                content=content,
                cms_enabled=cms_enabled,
            )

        try:
            pages = getContent("helpCentreInformation")
            if checkEmptyList(pages):
                abort(404)
            text = ""
            for page in pages:
                if page["id"] == sub_category:
                    text = page["content"]
                    break
            if text == "":
                abort(404)
        except OSError as e:
            _page_not_found(e)
        escaped_text = escape(text)
        body = Markup(markdown.markdown(escaped_text))

        return render_template(
            "help_category.html",
            body=body,
            category_label=category_label,
            sub_category_label=sub_category_label,
            category=category,
            sub_category=sub_category,
            nav=help_centre_nav,
            cms_enabled=cms_enabled,
        )

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
        body = None
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
        cms_enabled=cms_enabled,
    )


def _get_category_labels(selected_category, selected_sub_category):
    if cms_enabled:
        contents = getContent("helpCentreStructure")["structure"]
        if checkEmptyList(contents):
            abort(404)
    else:
        with open(
            "./content/help_centre/help_centre.json", encoding="utf-8"
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


def _help_centre_nav(
    current_category,
):
    if cms_enabled:
        contents = getContent("helpCentreStructure")["structure"]
        if checkEmptyList(contents):
            abort(404)
    else:
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
