import json
from sys import argv
from contentful import Client
import os

MASTER_CDA_KEY = os.environ.get("MASTER_CDA_KEY")
SPACE_ID = os.environ.get("SPACE_ID")


def main(filepath, target_env):
    with open(
            f"./contentful-data/audits/{filepath}", encoding="utf-8"
    ) as changeset_file:
        changeset = json.load(changeset_file)
    change_add, change_edit, change_delete, change_data = parse_changeset(changeset, target_env)
    build_report(change_add, change_edit, change_delete, change_data, filepath)
    print("audit_report.txt created")


def parse_changeset(json_data, target_env):
    client = Client(SPACE_ID, MASTER_CDA_KEY, environment=target_env)
    change_add = 0
    change_edit = 0
    change_delete = 0
    change_data = []
    items = json_data["items"]
    for dictionary in items:
        for key, value in dictionary.items():
            if key == "changeType":
                match value:
                    case "add":
                        change_add += 1
                    case "edit":
                        change_edit += 1
                    case "delete":
                        change_delete += 1
            if key == "data":
                new_dict = {"entry_id": value["sys"]["contentType"]["sys"]["id"], "fields": value["fields"]}
                entry = client.entry(value["fields"]["id"]["en-US"])
                print(entry)
                change_data.append(new_dict)
    return change_add, change_edit, change_delete, change_data


def build_report(add, edit, delete, data, name):
    with open('audit_report.txt', 'w', encoding="utf-8"
              ) as file:
        name = name.split('-')
        file.write(f"{name[0]} to {name[1]} Audit report:\n\n")
        file.write(f"Number of Entries added: {add}\n")
        file.write(f"Number of Entries edited: {edit}\n")
        file.write(f"Number of Entries deleted: {delete}\n\n")
        file.write("----------------------------------------------------------------\n\n")
        file.write("Summary of contents changed:\n\n")
        for count, entry in enumerate(data, start=1):
            file.write(f"Entry: {count}\n")
            file.write(f"Entry type: {entry['entry_id']}\n\n")
            for key, field in entry["fields"].items():
                file.write(f"Field Name: {key}\nField Data: {field['en-US']}\n\n")
            file.write("----------------------------------------------------------------\n\n")
        file.write("End of Report")
        file.close()


if __name__ == "__main__":
    main(argv[1], argv[2])
