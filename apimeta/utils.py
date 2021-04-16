def without_provided_keys(d: dict, keys: set) -> dict:
    """Return dict without provided keys"""
    return {x: d[x] for x in d if x not in keys}
