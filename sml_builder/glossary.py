import re
from json import dump, loads
from os import listdir, makedirs, path

from _jsonnet import evaluate_file  # pylint: disable=no-name-in-module
from flask import render_template

from sml_builder import app
from sml_builder.cms import getContent
from sml_builder.utils import checkEmptyList, get_feature_config

from .utils import _page_not_found

content_management = get_feature_config("content_management")


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


@app.route("/resources/glossary")
def display_glossary():
    glossary_list = []
    nav_options_list = []
    glossary_dir = "./content/glossary"
    if content_management["enabled"]:
        contents = getContent("glossaryEntry")
        if checkEmptyList(contents):
            _page_not_found("Glossary content not found")
        glossary_dir = "./contentful_content/glossary/"
        makedirs(path.dirname(glossary_dir), exist_ok=True)
        for i in contents:
            with open(
                f'./contentful_content/glossary/{i["name"]}.jsonnet',
                "w",
                encoding="UTF-8",
            ) as f:
                dump(i["glossary_content"], f)

    try:
        for file in listdir(glossary_dir):
            glossary_term = loads(evaluate_file(f"{glossary_dir}/{file}"))
            letter_value = (
                glossary_term["letter"].upper()
                if "letter" in glossary_term
                else glossary_term["term"][0].upper()
            )
            glossary_list.append(
                {
                    "term": glossary_term["term"],
                    "hash": convert_term(glossary_term["term"]),
                    "letter": letter_value,
                    "related": (
                        glossary_term["related"] if "related" in glossary_term else []
                    ),
                    "external_links": (
                        glossary_term["external_links"]
                        if "external_links" in glossary_term
                        else []
                    ),
                    "meaning": glossary_term["meaning"],
                }
            )
            nav_options_list.append(letter_value)

        nav_options = sorted(list(set(nav_options_list)))
        glossary = sorted(glossary_list, key=lambda d: d["term"].lower())
    except OSError as e:
        _page_not_found(e)
    return render_template(
        "glossary.html", page={"glossary": glossary, "nav_options": nav_options}
    )
