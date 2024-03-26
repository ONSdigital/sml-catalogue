# Function to search for partial matches
def search_partial(data_frame, query):
    result = data_frame[
        data_frame.apply(
            lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1
        )
    ]

    return result
