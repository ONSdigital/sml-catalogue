import re
from json import load

from flask import abort, url_for

from sml_builder import app


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


def _page_not_found(error):
    print(error)
    abort(404)


# For use with code optioning. This function reads the state of the specified feature from the feature.json file.
def get_feature_config(feature_name: str):
    with open("config/feature.json", "r", encoding="utf-8") as features_file:
        features = load(features_file)["features"]

    try:
        return features[feature_name]
    except KeyError as e:
        raise KeyError(f"Feature '{feature_name}' not found in features.") from e


def category_labels(file_path, selected_category, selected_sub_category):
    with open(file_path, encoding="utf-8") as help_contents_file:
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


def contents_helper(contents):
    categories = []
    for category in contents[
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
    return categories
