import difflib
import json
import os
from sys import argv

from contentful import Client

MASTER_CDA_KEY = os.environ.get("MASTER_CDA_KEY")
SPACE_ID = os.environ.get("SPACE_ID")


def main(filepath, target_env):
    with open(
        f"../contentful-data/audits/{filepath}", encoding="utf-8"
    ) as changeset_file:
        changeset = json.load(changeset_file)
    change_add, change_edit, change_delete, change_data = parse_changeset(
        changeset, target_env
    )
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
        new_dict = {}
        match dictionary["changeType"]:
            case "add":
                change_add += 1
            case "update":
                change_edit += 1
            case "delete":
                change_delete += 1
        if dictionary["changeType"] == "add":
            final_text = dictionary["data"]["sys"]["contentType"]["sys"]["id"] + "\n\n"
            for key, value in dictionary["data"]["fields"].items():
                final_text += f'<span style="color: green;">+ {key}</span>\n<span style="color: green;">+ {value["en-US"]}</span>\n\n'
            change_data.append(final_text)
        elif dictionary["changeType"] == "update":
            for patch in dictionary["patch"]:
                # get content element from path
                string = patch["path"]
                string = string[8:-6]
                new_dict.update({string: patch["value"]})
            entry = client.entry(dictionary["entity"]["sys"]["id"])
            final_text = "ENTRY TITLE: " + entry.fields()["id"].title() + "\n"
            for key, value in new_dict.items():
                highlight_text = highlight_differences(entry.fields()[key], value)
                highlight_text = "\n" + key.title() + "\n" + highlight_text + "\n"
                final_text += highlight_text
            change_data.append(final_text)
        elif dictionary["changeType"] == "delete":
            entry = client.entry(dictionary["entity"]["sys"]["id"])
            final_text = "ENTRY TITLE: " + entry.fields()["id"].title() + "\n"
            for key, value in entry.fields().items():
                final_text += f'<span style="color: red;">- {key}</span>\n<span style="color: red;">- {value}</span>\n\n'
            change_data.append(final_text)
    return change_add, change_edit, change_delete, change_data


def build_report(add, edit, delete, data, name):
    # RTF header
    html_header = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Highlighted Differences</title>
        <style>
            body { font-family: Courier, monospace; white-space: pre; }
        </style>
    </head>
    <body>
    <pre>
    """
    html_footer = """
    </pre>
    </body>
    </html>
    """

    with open("../../audit_report.html", "w", encoding="utf-8") as file:
        name = name.split("-")
        file.write(html_header)
        file.write(f"{name[0].title()} to {name[1].title()} Audit report:\n\n")
        file.write(f"Number of Entries added: {add}\n")
        file.write(f"Number of Entries edited: {edit}\n")
        file.write(f"Number of Entries deleted: {delete}\n\n")
        file.write(
            "----------------------------------------------------------------\n\n"
        )
        file.write("Summary of contents changed:\n")
        file.write(
            "----------------------------------------------------------------\n\n"
        )
        for count, entry in enumerate(data, start=1):
            file.write(f"Entry: {count}\n")
            file.write(f"{entry}\n\n")
            file.write(
                "----------------------------------------------------------------\n\n"
            )
        file.write("End of Report")
        file.write(html_footer)
        file.close()


def highlight_differences(target_env_string, base_env_string, context=3):
    # context refers to the number of lines to buffer before and after a changed line
    diff = list(
        difflib.ndiff(target_env_string.splitlines(), base_env_string.splitlines())
    )
    result = []
    buffer = []
    in_context = False
    unchanged_count = 0

    for line_number, line in enumerate(diff):
        if line.startswith("  "):  # indicates unchanged line
            if in_context:
                buffer.append(line)
                unchanged_count += 1
                if unchanged_count > context:
                    buffer.pop(0)
            else:
                buffer.append(line)
                if len(buffer) > context:
                    buffer.pop(0)
        else:
            if buffer:
                result.extend(
                    buffer[-context:]
                )  # Include the last 'context' lines before the change
                buffer = []
            if line.startswith("+ "):
                result.append(
                    f'<span style="color: green;">{line}</span>'
                )  # Green for additions
            elif line.startswith("- "):
                result.append(
                    f'<span style="color: red;">{line}</span>'
                )  # Red for deletions
            elif line.startswith("? "):
                result.append(
                    f'<span style="color: blue;">{line}</span>'
                )  # Yellow for context
            else:
                result.append(line)
            in_context = True
            unchanged_count = 0
            for line_after_change in range(
                1, context + 1
            ):  # Take the 3 lines after a change
                if line_number + line_after_change < len(diff) and diff[
                    line_number + line_after_change
                ].startswith("  "):
                    result.append(diff[line_number + line_after_change])
                else:
                    break
    return "\n".join(result)


if __name__ == "__main__":
    main(argv[1], argv[2])
