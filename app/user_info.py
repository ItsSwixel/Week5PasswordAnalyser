import datetime

def get_userinfo():

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    date = input("Please enter your date of birth in YYYY-MM-DD format: ")
    year, month, day = map(int, date.split("-"))
    birthday = datetime.date(year, month, day)

    password = input("Please enter your password: ")

    return first_name, last_name, birthday, password

if __name__ == '__main__':

    first_name, last_name, birthday, password = get_userinfo()

    print("Your name: ", first_name, last_name)
    print("Your birthday: ", birthday)
    print("Your password: ", password)
