import re
from flask import abort
from sml_builder import app


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


def _page_not_found(error):
    print(error)
    abort(404)
