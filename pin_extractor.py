"""Module providing a function for extracting pins."""

def pin_extractor(poems):
    """Function implementing the pin extractor."""
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

POEM = """Stars and the moon
shine in the sky
white and
until the end of the night"""

POEM2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
POEM3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([POEM, POEM2, POEM3]))
