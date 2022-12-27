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

def getContent(contentType):
    content_type = client.content_type(contentType)
    entries_by_content_type = getEntriesByContentType(content_type)
    content = compileContent(entries_by_content_type)

    return content

def getEntriesByContentType(contentType):
    entries_by_content_type = client.entries({"content_type": contentType.id})

    return entries_by_content_type

def compileContent(entries_by_content_type):
    content = dict()

    for entry in entries_by_content_type:
        content_type = entry.sys["content_type"].id
        entry_fields = entry.fields()
        content[content_type] = entry_fields

    return content


def getHelpCentre():
    pass
