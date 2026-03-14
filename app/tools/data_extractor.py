def extract_key_data(data):
    cleaned = []

    for d in data:
        cleaned.append(d.[:500])

    return cleaned