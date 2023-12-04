import os
from json import loads
from os import listdir

from _jsonnet import evaluate_file  # pylint: disable=no-name-in-module
from flask import render_template

from sml_builder import app
from sml_builder.env_config import EnvConfig

from .utils import _page_not_found, convert_term

environment = os.environ.get("ENV_NAME", "dev")

env_name = EnvConfig.get_environment_ga_code(environment)


@app.route("/resources/glossary")
def display_glossary():
    glossary_list = []
    nav_options_list = []
    glossary_dir = "./content/glossary"
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
                    "related": glossary_term["related"]
                    if "related" in glossary_term
                    else [],
                    "external_links": glossary_term["external_links"]
                    if "external_links" in glossary_term
                    else [],
                    "meaning": glossary_term["meaning"],
                }
            )
            nav_options_list.append(letter_value)

        nav_options = sorted(list(set(nav_options_list)))
        glossary = sorted(glossary_list, key=lambda d: d["term"].lower())
    except OSError as e:
        _page_not_found(e)
    return render_template(
        "glossary.html",
        page={"glossary": glossary, "nav_options": nav_options, "env_name": env_name},
    )
