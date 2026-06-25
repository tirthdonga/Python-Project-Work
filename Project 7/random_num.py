import random

def random_num():
    try:
        start = int(input("Enter start range: "))
        end = int(input("Enter end range: "))

        result = random.randint(start, end)
        
        print(f"Random Integer: {result}")
            
    except ValueError:
        print("Error: Please enter valid integers.")

def random_list():
    try:
        count = int(input("How many numbers do you want in your list? "))
        start = int(input("Enter start range: "))
        end = int(input("Enter end range: "))

        random_list = [random.randint(start, end) for _ in range(count)]
        
        print(f"Generated List: {random_list}")
            
    except ValueError:
        print("Error: Please enter valid integers.")

def generate_password():
    try:
        length = int(input("Enter password length: "))

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = "!@#$%^&*()-_=+"
        
        characters = letters + digits + symbols

        password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"Your random password is: {password}")
            
    except ValueError:
        print("Error: Please enter a valid integer for the length.")

def generate_otp():
    
    digits = "0123456789"
    otp = ""

    for i in range(6):
        otp = otp + random.choice(digits)
        
    print(f"Your Generated OTP is: {otp}")

