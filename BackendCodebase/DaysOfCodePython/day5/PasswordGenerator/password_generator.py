# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


if nr_letters == 0 and nr_symbols == 0 and nr_numbers == 0:
    print(f"You did not enter the criteria for creating a password.")
else:
    print(f"You can choose between an easy level and a hard level of password.")
    nr_level = int(input(
        f"Enter a number to generate passwords. Easy 1, Hard 2\n"))

    password_list = []

    # letters
    pick_letters = ""
    for pick in range(1, nr_letters + 1):
        password_list += random.choice(letters)

    # symbols
    pick_symbols = ""
    for pick in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    # nums
    pick_nums = ""
    for pick in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    password = ""
    for char in password_list:
        password += char

    # Easy Level - Order not randomised:
    if nr_level == 1:
        print(f"Here is your password: {password}")
    # Hard Level - Order of characters randomised:
    elif nr_level == 2:
        random.shuffle(password_list)
        random_password = ""
        for char in password_list:
            random_password += char
        print(f"Here is your password: {random_password}")
    elif nr_level > 2 or nr_level < 1:
        print(f"Maybe you entered the wrong password level. Please try again.")
