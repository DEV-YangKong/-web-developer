import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

tool = [rock, paper, scissors]

user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)
choice = [int(user_choice), int(computer_choice)]

print("\nuser chose:\n" + tool[choice[0]])
print("\ncomputer chose:\n" + tool[choice[1]])

if choice[0] == choice[1]:
    print("You draw!")
elif choice[0] == 0 and choice[1] == 2:
    print("You win!")
elif choice[0] == 2 and choice[1] == 0:
    print("You lose!")
elif choice[0] < choice[1]:
    print("You lose!")
elif choice[0] > choice[1]:
    print("You win!")
elif choice[0] > 2 or choice[0] < 0:
    print("You typed an invalid number! Try again.")
