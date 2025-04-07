import unittest
from password_validator import validate_password

class TestPasswordValidator(unittest.TestCase):
    
    # Test for a valid password
    def test_valid_password(self):
        self.assertTrue(validate_password("Abc1234!"))  

    # Test for a password that is too short
    def test_invalid_length_short(self):
        self.assertFalse(validate_password("A1!a123"))  

    # Test for a password that is too long
    def test_invalid_length_long(self):
        self.assertFalse(validate_password("A1!a123456789012345678")) 

    # Test for a password missing uppercase letters
    def test_missing_uppercase(self):
        self.assertFalse(validate_password("abc1234!"))  

    # Test for a password missing lowercase letters
    def test_missing_lowercase(self):
        self.assertFalse(validate_password("ABC1234!"))  

    # Test for a password missing digits
    def test_missing_digit(self):
        self.assertFalse(validate_password("Abcdefgh!")) 

    # Test for a password missing special characters
    def test_missing_special_char(self):
        self.assertFalse(validate_password("Abc12345")) 

    # Test for a password with invalid characters (like space)
    def test_invalid_character(self):
        self.assertFalse(validate_password("A Bc1234!"))

    # Test for a password with consecutive identical characters
    def test_consecutive_identical_characters(self):
        self.assertFalse(validate_password("AAABBBCCC"))  

    # Test for a valid password with max length
    def test_valid_max_length(self):
        self.assertTrue(validate_password("Abc1234!aBcd1234!")) 

if __name__ == '__main__':
    unittest.main()
