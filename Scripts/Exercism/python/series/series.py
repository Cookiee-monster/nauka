def slices(series, length):
    if length <= 0:
        raise ValueError("Length has to be at least 1")
    elif length > len(series) or len(series) == 0:
        raise ValueError("Length has to be larger than len of series")
    elif length == len(series):
        return [series]
    else:
        result = []
        for i in range(0, len(series) - length + 1):
            result.append(series[i:i+length])
        return result
