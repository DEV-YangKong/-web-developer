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

    # letters
    pick_letters = ""
    for pick in range(1, nr_letters + 1):
        pick_letters += random.choice(letters)

    # symbols
    pick_symbols = ""
    for pick in range(1, nr_symbols + 1):
        pick_symbols += random.choice(symbols)

    # nums
    pick_nums = ""
    for pick in range(1, nr_numbers + 1):
        pick_nums += random.choice(numbers)

    # Easy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    total_easy = pick_letters + pick_symbols + pick_nums

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    total_hard = ""
    for pick in range(1, len(total_easy) + 1):
        total_hard += random.choice(total_easy)

    if nr_level == 1:
        print(f"Here is your password: {total_easy}")
    elif nr_level == 2:
        print(f"Here is your password: {total_hard}")
    elif nr_level > 2 or nr_level < 1:
        print(f"Maybe you entered the wrong password level. Please try again.")
