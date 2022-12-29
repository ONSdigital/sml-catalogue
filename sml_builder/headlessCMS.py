import contentful

client = contentful.Client("ldcm7uk1vtxb", "kYeKazwcxKIM7neRynQ9UdTRbiZMsMbqy2SQV4PZfWI")

# Retrieves all content from contentful
# def getMethodsCatalogue():
#     content = dict()
    
#     content_types = client.content_types()

#     for content_type in content_types:
#         entries_by_content_type = client.entries({"content_type": content_type.id})
#         for entry in entries_by_content_type:
#             content_type = entry.sys["content_type"].id
#             entry_fields = entry.fields()
#             content[content_type] = entry_fields

#     print(content)

#     return content

# The function that retrieves and returns the content from contentful
def getContent(contentType, isTable):
    content_type = client.content_type(contentType)
    entries_by_content_type = getEntriesByContentType(content_type)
    if isTable:
        content = compileContentTable(entries_by_content_type)
    else:
        content = compileContent(entries_by_content_type)

    return content

# Gets the entries for the type of content passed into the function
def getEntriesByContentType(contentType):
    entries_by_content_type = client.entries({"content_type": contentType.id})

    return entries_by_content_type

# Compiles all the entries and puts in a dictionary to be used later in the HTML pages
def compileContent(entries_by_content_type):
    content = dict()

    for entry in entries_by_content_type:
        # content_type = entry.sys["content_type"].id
        entry_fields = entry.fields()
        # content[content_type] = entry_fields

    # print(content)
    return entry_fields

def compileContentTable(entries_by_content_type):
    content = []

    for entry in entries_by_content_type:
        # content_type = entry.sys["content_type"].id
        entry_fields = entry.fields()
        # content[content_type] = entry_fields
        content.append(entry_fields)

    # print(content)
    return content