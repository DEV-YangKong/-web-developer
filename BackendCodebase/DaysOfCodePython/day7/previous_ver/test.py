import random

word_list = ["hi", "hey", "yes"]

chosen_word = random.choice(word_list)

chosen_letter = []
for word in chosen_word:
    chosen_letter += word
print(chosen_letter)

answer = []

result = []
life = []
print(f"answer {answer}")

while not chosen_letter == answer or len(life) > 5:
    user_guess = input("Guess a letter : ").lower()
    i = ""
    for i in chosen_letter:
        if len(life) <= 5:
            if i == user_guess:
                print("Right")
                print(answer)
            elif not i == user_guess:
                print("Wrong")
                print(answer)
    print(f"answer is {answer}. You are life is {len(life)}")

    if answer == chosen_letter or len(life) > 5:
        print("game over")
