# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# 📌 my solution 📌
max_age = 90
years_remaining = max_age - int(age)
days = years_remaining * 365
weeks = years_remaining * 52
month = years_remaining * 12

print(f"You have {days} days, {weeks} weeks, and {month} months left.")

############################

# 📌 better solution : 나이부터 정수로 만드는게 더 보기 좋은 것 같다.
# 최대 나이는 굳이 정수로 변수 설정할 필요가 있을까?
# 프린트 전에 변수 설정으로 해주니 깔끔하다. 길더라도 변수의 뜻을 알기 쉽게 만들자. 📌
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
month_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months left."
print(message)
