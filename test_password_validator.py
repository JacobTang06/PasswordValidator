from password_validator import validate_password

class TestPasswordValidator:

    def test_password_length(self):
        assert validate_password("Val123!") == False
        assert validate_password("ValidatePassword12345!") == False

    def test_password_uppercase_letter(self):
        assert validate_password("validpass123!") == False

    def test_password_lowercase_letter(self):
        assert validate_password("VALIDPASS123!") == False
    
    def test_password_digit(self):
        assert validate_password("ValidPass!") == False

    def test_password_special_char(self):
        assert validate_password("ValidPass123") == False

    def test_password_invalid_char(self):
        assert validate_password("Invalid<Pass123!") == False
        assert validate_password("Invalid Pass123!") == False
        assert validate_password("InvalidPass123!]") == False

    def test_password_repeated_char(self):
        assert validate_password("InvalidPasss123!") == False
        assert validate_password("InvalidddddPass123!") == False

    def test_password_success(self):
        assert validate_password("ValidPass123!") == True

if __name__ == "__main__":
    tester = TestPasswordValidator()
    tester.test_password_length()
    tester.test_password_uppercase_letter()
    tester.test_password_lowercase_letter()
    tester.test_password_digit()
    tester.test_password_special_char()
    tester.test_password_invalid_char()
    tester.test_password_repeated_char()
    tester.test_password_success()
    print("All tests passed")
