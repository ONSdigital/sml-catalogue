import re
from sml_builder import app


@app.template_filter("convert_name")
def convert_term(value):
    converted = re.sub("[^0-9a-z]+", "-", value.lower())
    return converted


def checkTypeList(data):
    if isinstance(data, list):
        return True
    return None


def checkEmptyList(data):
    if not data:
        return True
    return None
