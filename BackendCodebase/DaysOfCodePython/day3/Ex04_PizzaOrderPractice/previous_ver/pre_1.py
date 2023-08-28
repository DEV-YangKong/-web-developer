# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

########## 3-06-24 ##########

# 문자열 포맷팅 이용해서 좀 더 깔끔하고 가독성 좋은 코드로 개선

small = 15
medium = 20
large = 25

pepp_s = 2
pepp_ml = 3
cheese = 1

bill = "Your final bill is: ${}."

if size == "S" or size == "s":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            syy = small + pepp_s + cheese
            print(bill.format(syy))
        elif extra_cheese == "N" or extra_cheese == "n":
            syn = small + pepp_s
            print(bill.format(syn))
    elif add_pepperoni == "N" or "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            sny = small + cheese
            print(bill.format(sny))
        elif extra_cheese == "N" or extra_cheese == "n":
            snn = small
            print(bill.format(snn))

if size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            myy = medium + pepp_ml + cheese
            print(bill.format(myy))
        elif extra_cheese == "N" or extra_cheese == "n":
            myn = medium + pepp_ml
            print(bill.format(myn))
    elif add_pepperoni == "N" or add_pepperoni == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            mny = medium + cheese
            print(bill.format(mny))
        elif extra_cheese == "N" or extra_cheese == "n":
            mnn = medium
            print(bill.format(mnn))

if size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            lyy = large + pepp_ml + cheese
            print(bill.format(lyy))
        elif extra_cheese == "N" or extra_cheese == "n":
            lyn = large + pepp_ml
            print(bill.format(lyn))
    elif extra_cheese == "N" or extra_cheese == "n":
        if extra_cheese == "Y" or extra_cheese == "y":
            lny = large + cheese
            print(bill.format(lny))
        elif extra_cheese == "N" or extra_cheese == "n":
            lnn = large
            print(bill.format(lnn))
