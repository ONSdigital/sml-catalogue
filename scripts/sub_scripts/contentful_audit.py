import difflib
import json
import os
from sys import argv

from contentful import Client

MASTER_CDA_KEY = os.environ.get("MASTER_CDA_KEY")
SPACE_ID = os.environ.get("SPACE_ID")


def main(filepath, target_env, base_env):
    with open(
        f"../contentful-data/audits/{filepath}", encoding="utf-8"
    ) as changeset_file:
        changeset = json.load(changeset_file)
    (
        change_add,
        change_edit,
        change_delete,
        add_sections,
        edit_sections,
        delete_sections,
        change_data,
        change_json,
    ) = parse_changeset(changeset, target_env, base_env)
    build_html(
        change_add,
        change_edit,
        change_delete,
        add_sections,
        edit_sections,
        delete_sections,
        change_data,
        filepath,
    )
    build_json(
        change_add,
        change_edit,
        change_delete,
        add_sections,
        edit_sections,
        delete_sections,
        change_json,
        filepath,
    )
    print("audit_reports created")


def parse_changeset(json_data, target_env, base_env):
    target_client = Client(SPACE_ID, MASTER_CDA_KEY, environment=target_env)
    base_client = Client(SPACE_ID, MASTER_CDA_KEY, environment=base_env)
    change_add = 0
    add_sections = []
    change_edit = 0
    edit_sections = []
    change_delete = 0
    delete_sections = []
    change_data = []
    change_dict = []
    items = json_data["items"]
    for dictionary in items:
        match dictionary["changeType"]:
            case "add":
                change_add += 1
                add_sections.append(
                    base_client.entry(dictionary["entity"]["sys"]["id"]).fields()[
                        "api_name"
                    ]
                )
            case "update":
                change_edit += 1
                edit_sections.append(
                    target_client.entry(dictionary["entity"]["sys"]["id"]).fields()[
                        "api_name"
                    ]
                )
            case "delete":
                change_delete += 1
                delete_sections.append(
                    target_client.entry(dictionary["entity"]["sys"]["id"]).fields()[
                        "api_name"
                    ]
                )
        if dictionary["changeType"] == "add":
            entry = base_client.entry(dictionary["entity"]["sys"]["id"])
            final_text = "ENTRY TITLE: " + entry.fields()["api_name"].title() + "\n"
            section_title = entry.fields()["api_name"].split("/")
            json_entry = {
                "Change_type": "add",
                "Section": section_title[0],
                "Change_Title": section_title[1],
                "Change_Summary": {},
            }
            for key, value in dictionary["data"]["fields"].items():
                final_text += f'<span style="color: green;">+ {key}</span>\n<span style="color: green;">+ {value["en-US"]}</span>\n\n'
                json_entry["Change_Summary"][key] = value["en-US"]
            change_data.append(final_text)
            change_dict.append(json_entry)
        elif dictionary["changeType"] == "update":
            entry = target_client.entry(dictionary["entity"]["sys"]["id"])
            base_entry = base_client.entry(dictionary["entity"]["sys"]["id"]).fields()
            final_text = "ENTRY TITLE: " + entry.fields()["api_name"].title() + "\n"
            section_title = entry.fields()["api_name"].split("/")
            json_entry = {
                "Change_type": "edit",
                "Section": section_title[0],
                "Change_Title": section_title[1],
                "Change_Summary": {},
            }
            for key, value in base_entry.items():
                highlight_text = highlight_differences(entry.fields()[key], value)
                highlight_text = "\n" + key.title() + "\n" + highlight_text + "\n"
                final_text += highlight_text
                json_entry["Change_Summary"]["original_" + key] = entry.fields()[key]
                json_entry["Change_Summary"]["new_" + key] = value
            change_data.append(final_text)
            change_dict.append(json_entry)
        elif dictionary["changeType"] == "delete":
            entry = target_client.entry(dictionary["entity"]["sys"]["id"])
            final_text = "ENTRY TITLE: " + entry.fields()["api_name"].title() + "\n"
            section_title = entry.fields()["api_name"].split("/")
            json_entry = {
                "Change_type": "delete",
                "Section": section_title[0],
                "Change_Title": section_title[1],
                "Change_Summary": {},
            }
            for key, value in entry.fields().items():
                final_text += f'<span style="color: red;">- {key}</span>\n<span style="color: red;">- {value}</span>\n\n'
                json_entry["Change_Summary"][key] = value
            change_data.append(final_text)
            change_dict.append(json_entry)
    return (
        change_add,
        change_edit,
        change_delete,
        add_sections,
        edit_sections,
        delete_sections,
        change_data,
        change_dict,
    )


def build_json(
    add, edit, delete, add_sections, edit_sections, delete_sections, data, name
):
    name = name.split("" "-")
    summary_dictionary = {
        "audit_report": f"{name[0].title()} to {name[1].title()} Audit report",
        "change_summary": {
            "added": {"total": add, "affected_sections": add_sections},
            "edited": {"total": edit, "affected_sections": edit_sections},
            "deleted": {"total": delete, "affected_sections": delete_sections},
        },
        "entries": data,
    }
    with open("audit_report.json", "w", encoding="utf-8") as file:
        json.dump(summary_dictionary, file, indent=4)
        file.close()


def build_html(
    add, edit, delete, add_sections, edit_sections, delete_sections, data, name
):
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
    add_string = ", ".join(add_sections)
    edit_string = ", ".join(edit_sections)
    delete_string = ", ".join(delete_sections)
    with open("audit_report.html", "w", encoding="utf-8") as file:
        name = name.split("" "-")
        file.write(html_header+"\n")
        file.write(f"{name[0].title()} to {name[1].title()} Audit report:\n\n")
        file.write(f"Number " f"of Entries added: {add}\n")
        file.write(f"Added entries: {add_string}\n\n")
        file.write(f"Number of Entries edited: {edit}\n")
        file.write(f"Edited entries: {edit_string}\n\n")
        file.write(f"Number of Entries deleted: {delete}\n\n")
        file.write(f"Deleted entries: {delete_string}\n\n")
        file.write(
            "--------------------------------------" "--------------------------\n\n"
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
    main(argv[1], argv[2], argv[3])
