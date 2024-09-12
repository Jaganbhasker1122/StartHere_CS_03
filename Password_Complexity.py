def check_password_strength(password):

    print("Welcome to the Password Complexity Checker")

    has_upperCase = False
    has_lowerCase = False
    has_digits = False
    has_specialChars = False
    specialChars = "!@#$%^&*(),.?\":{}|<>"

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upperCase = True
        elif char.islower():
            has_lowerCase = True
        elif char.isdigit():
            has_digits = True
        elif char in specialChars:
            has_specialChars = True

    
    length_criteria = len(password) >= 8

    strength = length_criteria + has_upperCase + has_lowerCase + has_digits + has_specialChars

    
    if strength == 5:
        print("Password is strong !!!")
    elif strength == 4:
        print("Password is medium !!!")
    else:
        print("Password is so Weak !!!")


password = input("Enter your Password to Check its Complexity: ")
check_password_strength(password)
