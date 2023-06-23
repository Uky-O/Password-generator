import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        meets_critera = True

        if numbers:
            meets_critera = has_number
        if special_characters:
            meets_criteria = meets_critera and has_special
    return pwd

min_lenght = int(input('Enter the minimum lenght:'))
p_number = input('Do you want to have a number (y/n)?'
                 'option:').lower()

password = generate_password(10, special_characters=False)
print(password)
