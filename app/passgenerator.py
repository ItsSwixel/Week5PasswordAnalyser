from random import *
import policy_checker
import password_checker
import user_info_checker
import datetime
# Needs a final check against personal information

# ------------------------GENERATE PASSWORD-----------------------------
generated_pass_list = []


def random_password(first_name, last_name, birthday):
    another_password = "Y"
    while another_password == "Y":
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

        password_list = password_letters + password_numbers + password_symbols

        shuffle(password_list)
        shuffle(password_list)
        password = "".join(password_list)
        if policy_checker.policy_check(password) == [] and password_checker.password_check(password) is False and user_info_checker.user_info_check(first_name, last_name, birthday, password) is False:
            print(password)
            generated_pass_list.append(password)
            another_password = input("Generate another password (Y/N): ").upper()
        if another_password == "N":
            break
    return generated_pass_list
