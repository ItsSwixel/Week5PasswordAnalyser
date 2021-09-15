"""
Takes the issues list and a boolean on whether personal info was found as parameters
Prints report to the screen
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
        return False


if __name__ == '__main__':
    report_generator([], False, False)
