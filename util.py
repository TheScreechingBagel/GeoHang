import re


# https://stackoverflow.com/a/69099798
def remove_accents(old: str) -> str:
    """Removes common accent characters, in lowercase"""
    # new = old.lower()
    new = old

    new = re.sub(r"[àáâãäå]", "a", new)
    new = re.sub(r"[èéêë]", "e", new)
    new = re.sub(r"[ìíîï]", "i", new)
    new = re.sub(r"[òóôõö]", "o", new)
    new = re.sub(r"[ùúûü]", "u", new)

    new = re.sub(r"[ÀÁÂÃÄÅ]", "A", new)
    new = re.sub(r"[ÈÉÊË]", "E", new)
    new = re.sub(r"[ÌÍÎÏ]", "I", new)
    new = re.sub(r"[ÒÓÔÕÖ]", "O", new)
    new = re.sub(r"[ÙÚÛÜ]", "U", new)

    return new
