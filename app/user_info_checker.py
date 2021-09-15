import user_info

def user_info_check(first_name, last_name, birthday, password):
    short_fname = first_name[0 : 4]
    short_lname = last_name[0 : 4]

    if password.count(short_fname) > 0:
        return True
    elif password.count(short_lname) > 0:
        return True
    elif password.count(str(birthday.day)) > 0:
        return True
    elif password.count(str(birthday.month)) > 0:
        return True
    elif password.count(str(birthday.year)) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    first_name, last_name, birthday, password = user_info.get_userinfo()

    if user_info_check(first_name, last_name, birthday, password) == True:
        print("Your personal information was found within the password supplied!")
    else:
        print("Your password is free of personal information!")
