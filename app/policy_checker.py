"""
Policy guidelines:
- Password must be over 8 characters long
- Password must contain at least 1 uppercase letter
- Password must contain at least 1 number
- Password must contain at least 1 special character
- Password must not have 3 consecutive duplicate values
"""
import string

"""
Takes a string as a parameter
Returns a list containing all of the issues found, each as an entry
"""


def policy_check(password):
    last_char = None
    uppercase_counter = 0
    number_count = 0
    special_count = 0
    dupe_count = 0
    issues = []
    if len(password) < 8:
        issues.append("Password is not long enough")
    for letter in password:
        if letter in string.ascii_uppercase:
            uppercase_counter += 1
        if letter in string.digits:
            number_count += 1
        if letter in string.punctuation:
            special_count += 1

        if last_char is not None:
            if letter == last_char:
                dupe_count += 1
                if dupe_count >= 2 and "Password contains 3 or more consecutive duplicate values" not in issues:
                    issues.append("Password contains 3 or more consecutive duplicate values")
            else:
                dupe_count = 0
        last_char = letter
    if uppercase_counter == 0:
        issues.append("Password does not contain an uppercase letter")
    if number_count == 0:
        issues.append("Password does not contain a number")
    if special_count == 0:
        issues.append("Password does not contain a special character")

    return issues
