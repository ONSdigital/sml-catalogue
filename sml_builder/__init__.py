from flask import Flask, render_template, request, g, abort, escape

app = Flask(__name__)

app.jinja_env.add_extension("jinja2.ext.do")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

import sml_builder.method
