# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# 📌 my solution : 코드는 짧지만, 가독성이 떨어진다. 📌
sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum)

##########################

# 📌 better solution (1) 📌
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# 📌 better solution (2) 📌
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

result = first_digit + second_digit
print(result)
