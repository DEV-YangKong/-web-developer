# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

########## 👇 코드 개선 두 번째 👇 23/06/24 ##########

# 어차피 위에서 아래로 진행하기 때문에 변수 bill의 값을 재할당해도 됨. 일일히 변수 선언할 필요 X

small = 15
medium = 20
large = 25

pepp_s = 2
pepp_ml = 3
cheese = 1

message = "Your final bill is: ${}."

if size == "S" or size == "s":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = small + pepp_s + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = small + pepp_s
            print(message.format(bill))
    elif add_pepperoni == "N" or "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = small + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = small
            print(message.format(bill))

if size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = medium + pepp_ml + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = medium + pepp_ml
            print(message.format(bill))
    elif add_pepperoni == "N" or add_pepperoni == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = medium + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = medium
            print(message.format(bill))

if size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = large + pepp_ml + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = large + pepp_ml
            print(message.format(bill))
    elif extra_cheese == "N" or extra_cheese == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            bill = large + cheese
            print(message.format(bill))
        elif extra_cheese == "N" or extra_cheese == "n":
            bill = large
            print(message.format(bill))
