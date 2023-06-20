from flask_frozen import Freezer
from sml_builder import app

__version__ = "0.1.7"

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
