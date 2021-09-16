import user_info
import policy_checker
import password_checker
import report_gen
import database_store
import passgenerator
import user_info_checker
import sys


class UserClass:
    def __init__(self, data):
        self.first_name = data[0]
        self.last_name = data[1]
        self.birthday = data[2]
        self.password = data[3]

    def set_password(self):
        self.password = input("Please enter your next password: ")


def menu_options():
    print("""Please enter one of the following options: 
            1) Password Strength Checker
            2) Password Generator
            3) Exit""")
    menu_option = input(">>> ")
    while menu_option != '1' and menu_option != '2' and menu_option != '3':
        print("Please only enter one of the specified values.")
        print("""Please enter one of the following options: 
                    1) Password Strength Checker
                    2) Password Generator
                    3) Exit""")
        menu_option = input(">>> ")
    return menu_option


def menu():
    counter = 0
    finished = False
    menu_option = menu_options()
    while finished is False:
        if menu_option == '1':
            if counter == 0:
                user = UserClass(user_info.get_userinfo_password())
            else:
                user.set_password()
            issues = policy_checker.policy_check(user.password)
            common = password_checker.password_check(user.password)
            personal = user_info_checker.user_info_check(user.first_name, user.last_name, user.birthday, user.password)
            file_name = report_gen.report_generator(issues, personal, common, user.password)
            if file_name is not True and file_name is not False:
                database_store.data_store(user.first_name, user.last_name, user.birthday, user.password, file_name)
            else:
                database_store.data_store(user.first_name, user.last_name, user.birthday, user.password)

        elif menu_option == '2':
            if counter == 0:
                user = UserClass(user_info.get_userinfo_password())
            pass_list = passgenerator.random_password(user.first_name, user.last_name, user.birthday)
            for item in pass_list:
                database_store.data_store(user.first_name, user.last_name, user.birthday, item)

        elif menu_option == '3':
            sys.exit()

        again = input("\nWould you like to run the program again? Y or N ").upper()
        while again != "Y" and again != "N":
            print("Please only enter Y or N")
            again = input("\nWould you like to run the program again? Y or N ").upper()
        if again == "N":
            finished = True
        elif again == "Y":
            menu_option = menu_options()
            counter += 1


if __name__ == '__main__':
    menu()
