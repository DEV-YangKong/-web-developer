import random

word_list = ["hi", "hey", "yes"]

chosen_word = random.choice(word_list)

chosen_letter = []
for word in chosen_word:
    chosen_letter += word
print(f"chosenletter : {chosen_letter}")

answer = []

for blank in chosen_letter:
    answer.append("_")


while not answer == chosen_letter:
    i = ""
    print(f"Now the answer is : {answer}")
    user_guess = input("Guess a letter : ").lower()

    if user_guess in chosen_letter:
        for i in chosen_letter:
            if i == user_guess:
                if not i in answer:
                    if not "_" in answer[0]:
                        while "_" in answer:
                            answer.remove("_")
                            print("remove1")
                        else:
                            answer.append(i)
                    if "_" in answer[0]:
                        while "_" in answer:
                            answer.remove("_")
                            print("remove2")
                        answer.append(i)
                        while len(answer) < len(chosen_letter):
                            answer.append("_")

                elif i in answer:
                    print(f"You already choose {user_guess}")
            elif i != user_guess and len(answer) < len(chosen_letter):
                answer.append("_")
                print("append2")
    else:
        print("You're wrong")


print(f"Game Over. last answer is : {answer}")
