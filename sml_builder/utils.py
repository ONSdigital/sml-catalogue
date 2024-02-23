import re

from flask import abort

from sml_builder import app
from json import load


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


def _page_not_found(error):
    print(error)
    abort(404)

def get_feature_config(feature_name: str):
    with open("config/feature.json", "r", encoding="utf-8") as features_file:
        features = load(features_file)["features"]

    try:
        return features[feature_name]
    except KeyError:
        raise KeyError(f"Feature '{feature_name}' not found in features.")
