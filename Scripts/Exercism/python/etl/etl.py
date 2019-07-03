def transform(legacy_data):
    data = {}
    for points, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = points

    return data
