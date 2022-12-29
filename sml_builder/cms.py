import contentful

client = contentful.Client(
    "ldcm7uk1vtxb", "kYeKazwcxKIM7neRynQ9UdTRbiZMsMbqy2SQV4PZfWI"
)


# Returns the content depending on the content type
def getContent(contentType):
    content_type = client.content_type(contentType)
    entries_by_content_type = getEntriesByContentType(content_type)

    content = compileContent(entries_by_content_type)

    return content


# Returns the entries for the type of content passed into the function
def getEntriesByContentType(contentType):
    entries_by_content_type = client.entries({"content_type": contentType.id})

    return entries_by_content_type


# Returns all the entries
def compileContent(entries_by_content_type):
    entry_fields = []
    if (len(entries_by_content_type)) == 1:
        entry_fields = entries_by_content_type[0].fields()
    else:
        for entry in entries_by_content_type:
            entry_fields.append(entry.fields())

    return entry_fields
