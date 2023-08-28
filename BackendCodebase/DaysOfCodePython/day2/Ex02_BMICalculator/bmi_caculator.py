# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# 📌 my solution 📌
m = float(height)
kg = int(weight)

bmi = kg / (m ** 2)

print(int(bmi))

#########################

# 📌 better solution (1) : 따로 변수 설정하지않고, 식에서 바로 정수와 부동소수 설정할 수 있다. 📌

bmi = int(weight) / float(height) ** 2

print(int(bmi))

# 📌 better solution (2)  : 내 풀이 방식과 비슷하다 📌

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)
