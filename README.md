# PasswordValidator

1. How to run code/tests:
- First, set up your environment by making sure you have python3 installed.
- Then, locate the password_validator.py and test_password_validator.py files.
- Test the password_validator.py file directly by running the test_password_validator.py file on the command line or an IDE.
2. Trade-offs:
- Efficiency: The password is checked character by character for multiple requirements including character types and invalid characters. While this is efficient for relatively small strings, larger strings would take a lot more time and resources to validate. Since the max length of the password is 20 characters, checking character by character is fine in this scenario.
- Security Checks: The code ensures the password is valid, but doesn't check against common password leaks or dictionary words.
3. Assumptions:
- Function assumes that user input is case sensitive.
- Function assumes that the input type is a valid string.
- Function assumes that the password validation is language-agnostic.
