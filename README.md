# Password Complexity Checker

## Introduction

The **Password Complexity Checker** is a simple Python program designed to evaluate the strength of a user's password based on key criteria such as length, the presence of uppercase and lowercase letters, numbers, and special characters. This tool provides immediate feedback to users on whether their password is **Weak**, **Medium**, or **Strong**, helping them improve their password security.

## Features

- Checks the password for the following criteria:
  - Minimum length of 8 characters
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit (0-9)
  - Contains at least one special character (e.g., `!@#$%^&*()_+`)
  
- Provides feedback on password strength:
  - **Weak**: If the password meets fewer than 4 criteria.
  - **Medium**: If the password meets exactly 4 out of 5 criteria.
  - **Strong**: If the password meets all 5 criteria.

## Requirements

This project only requires a basic Python environment. No external libraries or packages are needed.

- Python 3.x

## How It Works

The program checks each character of the password to see if it satisfies the following conditions:

1. **Length**: The password must be at least 8 characters long.
2. **Uppercase Letters**: The password should contain at least one uppercase letter.
3. **Lowercase Letters**: The password should contain at least one lowercase letter.
4. **Numbers**: The password should contain at least one digit (0-9).
5. **Special Characters**: The password should contain at least one special character, such as `!@#$%^&*()`.

The strength of the password is determined by how many of these criteria are satisfied.

## Usage

1. Clone or download this repository.
2. Run the Python program:

python password_checker.py

Enter your Password to Check its Complexity:   


Welcome to the Password Complexity Checker


Enter your Password to Check its Complexity: Password123!


Password is strong !!!

## Test Cases

Here are some example passwords and their expected outcomes:

| Password        | Expected Result     |
| --------------- | ------------------- |
| `pass123`       | Weak Password       |
| `Password12`    | Medium Password     |
| `Password123!`  | Strong Password     |

