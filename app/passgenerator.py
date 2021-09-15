from random import *
import policy_checker

# ------------------------GENERATE PASSWORD-----------------------------
generated_pass_list = []


def random_password():
    another_password = "Y"
    while another_password == "Y":
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
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
        if policy_checker.policy_check(password) == []:
            print(password)
            generated_pass_list.append(password)
        else:
            random_password()
        another_password = input("Generate another password (Y/N): ").upper()

    return password


if __name__ == '__main__':
    random_password()
