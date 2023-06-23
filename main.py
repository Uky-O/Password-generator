from PassWFunction import generate_password

min_lenght = int(input('Enter the minimum lenght:'))
has_number = input('Do you want to have a number (y/n)?\noption:').lower() == 'y'
has_special = input('Do you want to have special characters?(y/n)\noption:').lower() == 'y'
if has_number == 'n':
    has_number = False
elif has_number == 'y':
    has_number = True
if has_special == 'n':
    has_special = False
elif has_special == 'y':
    has_special = True

password = generate_password(min_lenght, has_number, has_special)
print(f'The generator password is: {password}')
