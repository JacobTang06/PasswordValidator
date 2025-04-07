# PasswordValidator

Problem Statement
Create a Python function that validates a password based on specific rules, then design a test suite to verify its correctness.


Password Validation Requirements:
Length: Must be between 8 and 20 characters (inclusive).
Character Types: Must include at least:
1 uppercase letter
1 lowercase letter
1 numeric digit
1 special character from !@#$%^&*()
Invalid Characters: Must NOT contain spaces or any of <>{}[].
No Repeats: Must not have the same character repeated consecutively more than twice (e.g., aaa is invalid).
Tasks:
Implement the Validator Function
Write a Python function validate_password(password: str) -> bool that returns True if the password meets all criteria, else False.
Design Test Cases
Create a structured list of test cases (positive and negative) to cover:
All validation rules.
Edge cases (e.g., minimum/maximum length, boundary values).
Provide a brief description for each test case explaining what it verifies.
Automate the Tests (Optional but Recommended)
Write a script (using a framework like pytest or unittest) to execute your test cases automatically.
Documentation
Include a README.md explaining:
How to run your code/tests.
Any assumptions or trade-offs made during implementation.
Example Test Cases:
Example Test Cases: 

	# Positive Test Case 

	assert validate_password("ValidPass123!") == True 

# Negative Test Case (contains invalid character '<') 

	assert validate_password("Invalid<Pass123!") == False



Evaluation Criteria:

Code Quality
Readability and modularity.
Test Coverage
Completeness of test cases (are all rules and edge cases addressed?).
Accuracy
Does the validator function correctly implement all rules?
Bonus Points
Use of parameterized tests.
Handling unexpected inputs (e.g., None, non-string types).
Considering security implications (e.g., timing attacks).
Submission Instructions:
Provide a GitHub/GitLab repo link or a ZIP file containing:
password_validator.py (implementation).
test_password_validator.py (test cases/scripts).
README.md (documentation).
Deadline: 24 hours from receipt
