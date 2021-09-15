"""
- Takes the issues list and a boolean on whether personal info was found and a boolean for whether it was in the
password list as parameters
- Prints report to the screen
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
            file_gen(issues, info_found, common_found)
        else:
            return False


def file_gen(issues, info_found, common_found):
    with open("password_report.txt", "w") as f:
        f.write("This is the generated file password report: \n")
        for item in issues:
            f.write(str(item) + "\n")
        if info_found:
            f.write("Personal information was found in your password\n")
        if common_found:
            f.write("Your password was found in the top 10,000 most common passwords\n")


if __name__ == '__main__':
    report_generator(["Password contains 3 or more consecutive duplicate values"], True, True)
