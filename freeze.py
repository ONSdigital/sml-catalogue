from flask_frozen import Freezer
from sml_builder import app

__version__ = "0.1.3"

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
