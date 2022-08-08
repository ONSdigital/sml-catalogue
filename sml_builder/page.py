from os import listdir
from flask import request, render_template, redirect, url_for, abort, g
from json import loads
from _jsonnet import evaluate_file
from sml_builder import app


@app.route("/help")
def help():
    return "help"


@app.route("/resources")
def resources():
    return render_template("about.html")
