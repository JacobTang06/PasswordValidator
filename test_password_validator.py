from password_validator import validate_password

class TestPasswordValidator:

    # Test with a password that has an invalid password length
    def test_password_length(self):
        assert validate_password("Val123!") == False
        assert validate_password("ValidatePassword12345!") == False

    # Test with a password that doesn't have at least one uppercase letter
    def test_password_uppercase_letter(self):
        assert validate_password("validpass123!") == False

    # Test with a password that doesn't have at least one lowercase letter
    def test_password_lowercase_letter(self):
        assert validate_password("VALIDPASS123!") == False
    
    # Test with a password that doesn't have at least one special character
    def test_password_digit(self):
        assert validate_password("ValidPass!") == False

    # Test with a password that doesn't have at least one special character
    def test_password_special_char(self):
        assert validate_password("ValidPass123") == False

    # Test with a password that has an invalid character
    def test_password_invalid_char(self):
        assert validate_password("Invalid<Pass123!") == False
        assert validate_password("Invalid Pass123!") == False
        assert validate_password("InvalidPass123!]") == False

    # Test with a password that has repeated consecutive characters
    def test_password_repeated_char(self):
        assert validate_password("InvalidPasss123!") == False
        assert validate_password("InvalidddddPass123!") == False

    # Test with a valid password
    def test_password_success(self):
        assert validate_password("ValidPass123!") == True

## Edge Cases

    # Test with an empty password
    def test_empty_password(self):
        assert validate_password("") == False 

    # Test with a null input (None in Python)
    def test_null_password(self):
        assert validate_password(None) == False  

    # Test with a password containing only digits
    def test_only_digits(self):
        assert validate_password("12345678") == False 

    # Test with a password containing only special characters
    def test_only_special_characters(self):
        assert validate_password("!@#$%^&*") == False 

    # Test with a password that has three consecutive identical characters (case sensitive)
    def test_consecutive_identical_characters(self):
        assert validate_password("AaABbbBccc") == False

if __name__ == "__main__":
    tester = TestPasswordValidator()
    tester.test_password_length()
    tester.test_password_uppercase_letter()
    tester.test_password_lowercase_letter()
    tester.test_password_digit()
    tester.test_password_special_char()
    tester.test_password_invalid_char()
    tester.test_password_repeated_char()
    tester.test_empty_password()
    tester.test_null_password()
    tester.test_only_digits()    
    tester.test_only_special_characters()
    tester.test_consecutive_identical_characters()
    print("All tests passed")
