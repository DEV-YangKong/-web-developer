# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

random_num = random.randint(0, len(names) - 1)
choice_person = names[random_num]

print(f"{choice_person} is going to buy the meal today!")
