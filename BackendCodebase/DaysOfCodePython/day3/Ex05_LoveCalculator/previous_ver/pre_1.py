# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

message_x = "Your score is {}, you go together like coke and mentos."
message_y = "Your score is {}, you are alright together."
message_z = "Your score is {}."

combined_name = name1.lower() + name2.lower()

count_true = combined_name.count(
    "t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")


count_love = combined_name.count(
    "l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

love_score = int(f"{count_true}{count_love}")

if love_score < 10 or love_score > 90:
    print(message_x.format(love_score))
elif love_score >= 40 and love_score <= 50:
    print(message_y.format(love_score))
else:
    print(message_z.format(love_score))
