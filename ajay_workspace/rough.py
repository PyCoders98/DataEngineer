    return [string for string, length in map(lambda s: (s, len(s)), strings) if length > threshold]
