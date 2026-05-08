def disemvowel(string_):
    result = ''
    for char in string_:
        if char not in "aeiouAEIOU":
            result += char
    return result
            