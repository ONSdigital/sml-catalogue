from flask_frozen import Freezer

from sml_builder import app

freezer = Freezer(app)
charset = {}
if __name__ == "__main__":
    freezer.freeze()
