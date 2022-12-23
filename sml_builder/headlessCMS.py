# Retrieves the content for the Methods Catalogue page
def getMethodsCatalogue():
    import contentful

    client = contentful.Client("ldcm7uk1vtxb", "kYeKazwcxKIM7neRynQ9UdTRbiZMsMbqy2SQV4PZfWI")

    content = dict()
    
    content_types = client.content_types()

    for content_type in content_types:
        entries_by_content_type = client.entries({"content_type": content_type.id})
        for entry in entries_by_content_type:
            content_type = entry.sys["content_type"].id
            entry_fields = entry.fields()
            content[content_type] = entry_fields

        # print("Content", content)

    print(content)

    return content