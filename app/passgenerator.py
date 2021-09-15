from random import *
# ------------------------GENERATE PASSWORD-----------------------------
generated_pass_list = []
def random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    shuffle(password_list)
    password = "".join(password_list)
    print(password)
    generated_pass_list.append(password)

    return password

def question():
    another_password = input("Generate another password (Y/N): ")
    return another_password

def more_password():

    while question() == "Y":
        random_password()


random_password()
print(more_password())

for i in range(len(generated_pass_list)):
    print(f" Password {i+1} contains the following issue(s): {policy_check(generated_pass_list[i])}")
