from os import listdir
from flask import render_template
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app


@app.route("/resources/glossary")
def display_glossary():
    glossary_list = []
    nav_options_list = []
    glossary_dir = "./content/glossary"
    for file in listdir(glossary_dir):
        glossary_term = loads(evaluate_file(f"{glossary_dir}/{file}"))
        glossary_list.append({
            "term": glossary_term["term"],
            "hash": glossary_term["hash"],
            "letter": glossary_term["letter"].upper(),
            "meaning": glossary_term["meaning"]
        })
        nav_options_list.append(glossary_term["letter"].upper())

    nav_options = sorted(list(set(nav_options_list)))
    glossary = sorted([dict(t) for t in {tuple(d.items()) for d in glossary_list}], key=lambda d: d['term'])
    return render_template("glossary.html", page={"glossary": glossary, "nav_options": nav_options})
