import re
from sml_builder import app


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


def checkTypeList(data):
    return isinstance(data, list)


def checkEmptyList(data):
    return not data
