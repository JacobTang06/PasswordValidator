def validate_password(password:str) -> bool:
    specialCharacters = '!@#$%^&*()'
    invalidCharacters = ' <>[]{}'
    if password is None:
        return False
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
        if password[i].upper() == password[i+1].upper() and password[i].upper() == password[i+2].upper():
            return False
    return True