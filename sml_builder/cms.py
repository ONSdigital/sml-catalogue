import os

import contentful
import os

# Will need a official contentful account for the project/ team, and then we can update
# the space_id, content_delivery_api_key
SPACE_ID = ""
CDA_KEY = ""

try:
    with open("cms_tokens.txt", "r") as file:
        CDA_KEY = file.readline()
        SPACE_ID = file.readline()
except FileNotFoundError:
    print("cms_tokens.txt file not found")
    SPACE_ID = os.environ.get("SPACE_ID")
    CDA_KEY = os.environ.get("CDA_KEY")
except Exception as e:
    print("Error reading cms_tokens.txt:", str(e))

client = contentful.Client(SPACE_ID, CDA_KEY)


# Returns the content depending on the content type
def getContent(contentType):
    content_type = client.content_type(contentType)
    # print("content_type: ", content_type)
    entries_by_content_type = getEntriesByContentType(content_type)
    # print("entries_by_content_type: ", entries_by_content_type)

    content = compileContent(entries_by_content_type)

    return content


# Gets the entries for the type of content passed into the function
def getEntriesByContentType(contentType):
    entries_by_content_type = client.entries({"content_type": contentType.id})
    # print("entries_by_content_type2: ", entries_by_content_type)

    return entries_by_content_type


# Returns all the content depending if it's a list of content such as items on a table
# or single item
def compileContent(entries_by_content_type):
    entry_fields = []
    if (len(entries_by_content_type)) == 1:
        entry_fields = entries_by_content_type[0].fields()
    else:
        for entry in entries_by_content_type:
            entry_fields.append(entry.fields())

    # print("entry_fields2: ", entry_fields)

    return entry_fields
