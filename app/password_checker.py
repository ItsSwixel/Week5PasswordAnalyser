import os


def password_check(password):
    with open(os.path.join(os.path.dirname(__file__), "10000_common.txt"), "r") as file:
        password_list = [line.strip() for line in file]

    for item in password_list:
        if item == password:
            return True
    return False
