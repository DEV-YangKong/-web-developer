# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

student_scores.sort()

for score in student_scores:
    score = score
print(f"The highest score in the class is: {score}")
