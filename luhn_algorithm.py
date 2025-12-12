"""Luhn Algorithm Implementation"""
def verify_card_number(card_number):
    """Function to verify a credit card number using the Luhn algorithm."""
    # Remove spaces and dashes
    clean_number = card_number.replace(" ", "").replace("-", "")

    # Ensure all characters are digits
    if not clean_number.isdigit():
        return "INVALID!"

    digits = [int(d) for d in clean_number]

    # Luhn algorithm
    total = 0
    # Start from rightmost digit, moving left
    # Use index offset trick: reverse the digits
    reversed_digits = digits[::-1]

    for i, digit in enumerate(reversed_digits):
        if i % 2 == 1:  # double every second digit (excluding check digit)
            doubled = digit * 2
            # If doubling is greater than 9, subtract 9
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit

    # Check validity
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
