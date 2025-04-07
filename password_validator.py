def validate_password(password:str) -> bool:
    specialCharacters = '!@#$%^&*()'
    invalidCharacters = ' <>[]{}'
    if len(password) < 8 or len(password) > 20:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in specialCharacters for char in password):
        return False
    if any(char in invalidCharacters for char in password):
        return False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] and password[i] == password[i+2]:
            return False
    return True