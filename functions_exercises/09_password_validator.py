import re
import string


def password_validator():
    given_password = input()
    val = True

    if len(given_password) < 6 or len(given_password) > 10:
        print(f'Password must be between 6 and 10 characters')
        val = False

    if not given_password.isalnum():
        print('Password must consist only of letters and digits')
        val = False

    if not any(char.isdigit() for char in given_password):
        print('Password must have at least 2 digits')
        val = False

    if val:
        print("Password is valid")


password_validator()
