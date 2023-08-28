import random

word_list = ["yangkong", "developer", "yessilver"]

chosen_word = random.choice(word_list)

chosen_letter = []
for word in chosen_word:
    chosen_letter += word
print(chosen_letter)
print(len(chosen_letter))

current = []
life = 0


while life <= 5:
    if chosen_letter == current or life > 5:
        print("game over")
    else:
        user_guess = input("Guess a letter : ").lower()
        pick = ""
        for pick in chosen_letter:
            if user_guess == pick and life <= 5:
                life -= 1
                current.append(user_guess)
                print(current)
            elif user_guess != pick and life <= 5:
                life += 1
print(f"{life} , {current}")
