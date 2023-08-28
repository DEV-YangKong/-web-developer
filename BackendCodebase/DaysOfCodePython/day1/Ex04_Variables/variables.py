# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

####################################
# 📌 my solution : 두 개의 병에 골라담기 📌
c = a
d = b
b = c
a = d

####################################

#  📌 better solution: 하나의 병에 담는게 더 효율적. 굳이 코드 한 줄 더 늘릴 필요 없음. 📌
c = a
a = b
b = c

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
