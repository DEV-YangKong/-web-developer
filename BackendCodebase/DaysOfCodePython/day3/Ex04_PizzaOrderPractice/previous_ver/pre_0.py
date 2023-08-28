# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

########## 👇 23/06/23 👇##########

small = 15
medium = 20
large = 25

pepp_s = 2
pepp_ml = 3
cheese = 1

if size == "S" or size == "s":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${small + pepp_s + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${small + pepp_s}.")
    elif add_pepperoni == "N" or "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${small + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${small}.")

if size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${medium + pepp_ml + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${medium + pepp_ml}.")
    elif add_pepperoni == "N" or add_pepperoni == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${medium + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${medium}.")

if size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${large + pepp_ml + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${large + pepp_ml}.")
    elif extra_cheese == "N" or extra_cheese == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"Your final bill is: ${large + cheese}.")
        elif extra_cheese == "N" or extra_cheese == "n":
            print(f"Your final bill is: ${large}.")
