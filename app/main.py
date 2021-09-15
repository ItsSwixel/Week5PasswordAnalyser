import user_info
import policy_checker
import password_checker
import report_gen
import database_store
import passgenerator
"""
Main script plan:
- Password Strength Checker
    - Check against personal info (SCRIPT BEING WRITTEN)
- Password generator
    - Check against personal info (SCRIPT BEING WRITTEN)
"""


def menu():
    first_name, last_name, birthday, password = user_info.get_userinfo()
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
    if menu_option == '1':
        issues = policy_checker.policy_check(password)
        common = password_checker.password_check(password)
        # Personal info check here
        file_name = report_gen.report_generator(issues, "Personal here", common)
        if file_name is not True and file_name is not False:
            database_store.data_store(first_name, last_name, birthday, password, file_name)
        else:
            database_store.data_store(first_name, last_name, birthday, password)
    elif menu_option == '2':
        pass_list = passgenerator.random_password()
        for item in pass_list:
            database_store.data_store(first_name, last_name, birthday, item)


if __name__ == '__main__':
    menu()
