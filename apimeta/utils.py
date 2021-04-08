def without_keys(d: dict, keys: set):
    """Return dict without keys"""
    return {x: d[x] for x in d if x not in keys}
