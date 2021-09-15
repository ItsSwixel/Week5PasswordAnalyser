import datetime
"""
- Takes the issues list and a boolean on whether personal info was found and a boolean for whether it was in the
password list as parameters
- Prints report to the screen
- Will send all data to a log file upon request and log file will have unique name
- returns True if password is strong, returns filename if its weak and they wanted it exports, returns False if its 
weak and no file was made
"""


def report_generator(issues, info_found, common_found):
    if len(issues) == 0 and not info_found and not common_found:
        print("Your password is strong!")
        return True
    else:
        print("Here is a report detailing why your password is weak: \n")
        if info_found:
            print("Personal information was found in your password")
        if common_found:
            print("Your password was found in the top 10,000 most common passwords")
        for item in issues:
            print(item)
        gen_file = input("\nWould you like your report generated into a file? Y or N  ")
        while gen_file.upper() != "Y" and gen_file.upper() != "N":
            print("Please only enter Y or N\n")
            gen_file = input("Would you like your report generated into a file? Y or N  ")
        if gen_file.upper() == "Y":
            file_name = file_gen(issues, info_found, common_found)
            return file_name
        else:
            return False


def file_gen(issues, info_found, common_found):
    basename = "password_report"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    file_name = "_".join([basename, suffix])
    with open(file_name, "w") as f:
        f.write("This is the generated file password report: \n")
        for item in issues:
            f.write(str(item) + "\n")
        if info_found:
            f.write("Personal information was found in your password\n")
        if common_found:
            f.write("Your password was found in the top 10,000 most common passwords\n")
    return file_name


if __name__ == '__main__':
    report_generator(["Password contains 3 or more consecutive duplicate values"], True, True)
