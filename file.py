import json
import sys
import os

assets = json.loads(sys.argv[1])
for asset in assets:
    if asset["name"] == "file.zip":
        os.environ["ASSET_URL"] = asset["url"]
        break
