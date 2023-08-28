# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

message_x = "Your score is {}, you go together like coke and mentos."
message_y = "Your score is {}, you are alright together."
message_z = "Your score is {}."

lower_name1 = name1.lower()
lower_name2 = name2.lower()

count_true_name1 = lower_name1.count(
    "t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e")
count_true_name2 = lower_name2.count(
    "t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")
score_true = count_true_name1 + count_true_name2

count_love_name1 = lower_name1.count(
    "l") + lower_name1.count("o") + lower_name1.count("v") + lower_name1.count("e")
count_love_name2 = lower_name2.count(
    "l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e")
score_love = count_love_name1 + count_love_name2

total_score = int(f"{score_true}{score_love}")

if total_score < 10 or total_score > 90:
    print(message_x.format(total_score))
elif total_score >= 40 and total_score <= 50:
    print(message_y.format(total_score))
else:
    print(message_z.format(total_score))
