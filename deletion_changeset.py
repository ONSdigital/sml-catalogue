from json import load, dump
import os
import time
import sys

if __name__ == "__main__":
    allowed_environments = ["dev", "preprod", "prod"]
    if len(sys.argv) == 3:
        target_environment = sys.argv[1]
        env_export_filepath = sys.argv[2]
    else:
        print(
            "Usage: python deletion_changeset.py <target_environment> <path_to_target_environment_export_file>"
        )
        sys.exit(1)
    if target_environment not in allowed_environments:
        print("Invalid environment. Allowed environments are dev, preprod, prod.")
        sys.exit(1)
    with open(
        "./contentful-data/migrations/deletion-changeset.json", encoding="utf-8"
    ) as deletion_changeset_file:
        deletion_changeset = load(deletion_changeset_file)
    with open(
        env_export_filepath,
        encoding="utf-8",
    ) as target_file:
        target_environment_data = load(target_file)
    unix_timestamp = int(time.time() * 1000)
    deletion_changeset["sys"]["createdAt"] = str(unix_timestamp)
    deletion_changeset["sys"]["target"]["sys"]["id"] = target_environment
    deletion_changeset["items"] = [
        {
            "changeType": "delete",
            "entity": {
                "sys": {"type": "Link", "linkType": "Entry", "id": item["sys"]["id"]}
            },
        }
        for item in target_environment_data["entries"]
        if item["sys"]["environment"]["sys"]["id"] == target_environment
    ]
    with open("./contentful-data/migrations/deletion-changeset.json", "w") as outfile:
        dump(deletion_changeset, outfile)
