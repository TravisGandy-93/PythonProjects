"""Module providing a function printing character statistics."""
FULL_DOT = '●'
EMPTY_DOT = '○'


def create_character(name, strength, intelligence, charisma):
    """Function implementing the character creation."""
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) > 10:
        return 'The character name is too long'
    if name.count(" ") > 0:
        return 'The character name should not contain spaces'
    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    if not all(num >= 1 for num in stats):
        return 'All stats should be no less than 1'
    if not all(num <= 4 for num in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    return f"{name}\nSTR {FULL_DOT * strength}{EMPTY_DOT * (10 - strength)}\nINT {FULL_DOT * intelligence}{EMPTY_DOT * (10 - intelligence)}\nCHA {FULL_DOT * charisma}{EMPTY_DOT * (10 - charisma)}"


print(create_character("ren", 4, 2, 1))
