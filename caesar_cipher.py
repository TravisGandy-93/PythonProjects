"""Module providing a function printing ciphered text."""

def caesar(text, shift, do_encrypt=True):
    """Function implementing the Caesar cipher."""
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not do_encrypt:
        shift = - shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    result = text.translate(translation_table)
    return result


def encrypt(text, shift):
    """Function implementing the Caesar cipher encryption."""
    return caesar(text, shift)


def decrypt(text, shift):
    """Function implementing the Caesar cipher decryption."""
    return caesar(text, shift, do_encrypt=False)

# Example usage:

NORMAL_TEXT = 'Caesar is found in unlikely places.'
encrypted_text = encrypt(NORMAL_TEXT, 7)
print(encrypted_text)

ENCRYPTED_TEXT = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(ENCRYPTED_TEXT, 13)
print(decrypted_text)
