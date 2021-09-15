"""
Main script plan:
- Take users personal info
- Show menu options
- Password Strength Checker
    - Enter password
    - Call policy_checker.py to check against policies and store issues list
    - Call password_checker.py store boolean
    - Check against personal info (SCRIPT TO BE WRITTEN)
    - Call report_gen.py sending output of all 3
    - Store all information in database (SCRIPT TO BE WRITTEN)
- Password generator
    - Generate password
    - Send it to policy_checker.py
    - Send it to password_checker.py
    - Check against personal info (SCRIPT TO BE WRITTEN)
    - Call report_gen.py
    - Ask if they want another password generated
"""