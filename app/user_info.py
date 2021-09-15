import datetime

def get_userinfo():

    while True:
            first_name = input("Please enter your first name: ")

            if len(first_name) > 20:
                print("\n First name is too large! \n")
            elif not first_name.isalpha():
                print("\n First name should only contain characters A-Z! \n")
            else:
                break

    while True:
            last_name = input("Please enter your last name: ")

            if len(last_name) > 20:
                print("\n Last name is too large! \n")
            elif not last_name.isalpha():
                print("\n Last name should only contain characters A-Z! \n")
            else:
                break

    while True:
        try:
            date = input("Please enter your date of birth in YYYY-MM-DD format: ")
            year, month, day = map(int, date.split("-"))
            birthday = datetime.date(year, month, day)
            break
        except ValueError:
            print("\n Wrong date format! \n")

    password = input("Please enter your password: ")

    return first_name, last_name, birthday, password


if __name__ == "__main__":

    first_name, last_name, birthday, password = get_userinfo()

    print("\nYour name: ", first_name, last_name)
    print("Your birthday: ", birthday)
    print("Your password: ", password)
