# Tip Calculator 팁 계산기
# This is a tip calculator program that calculates the amount each person should pay when splitting a bill with a tip. There are two approaches implemented in the code, and both are explained below.

##################################################################################
# First Approach
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating the bill with tip
bill_with_tip = f"1.{tip}"
each_pay = (bill / people) * float(bill_with_tip)

# Rounding the final amount to 2 decimal places
final_amount = round(each_pay, 2)

# Formatting the final amount with 2 decimal places
final_amount = "{:.2f}".format(each_pay)

# Creating the message to display
message = f"Each person should pay: ${final_amount}"
print(message)

# In the first approach, the code uses an f-string to calculate the bill with tip. 
# It prompts the user for the total bill, tip percentage, and the number of people to split the bill. 
# The bill amount is divided by the number of people, and the tip percentage is added to the result. 
# The final amount is rounded to 2 decimal places and formatted as a string with 2 decimal places. 
# The calculated amount is then displayed as a message.

# 첫 번째 접근 방식에서는 코드가 f-문자열을 사용하여 팁이 포함된 계산을 수행합니다.
# 사용자에게 총 청구액, 팁 비율 및 청구액을 나눌 사람 수를 입력 받습니다.
# 청구액은 사람 수로 나누고, 그 결과에 팁 비율이 더해집니다.
# 최종 금액은 소수점 이하 2자리로 반올림되고, 2자리로 형식화된 문자열로 변환됩니다.
# 계산된 금액은 메시지로 표시됩니다.
##################################################################################

##################################################################################
# Second Approach
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
new_percentage_tip = percentage_tip / 100 + 1
people = int(input("How many people to split the bill? "))

# Calculating the bill with tip
each_pay = (total_bill / people) * float(new_percentage_tip)

# Rounding the final amount to 2 decimal places
final_amount = round(each_pay, 2)

# Formatting the final amount with 2 decimal places
final_amount = "{:.2f}".format(each_pay)

# Creating the message to display
message = f"Each person should pay: ${final_amount}"
print(message)

# In the second approach, the code calculates the bill with tip using a different method. 
# It prompts the user for the total bill, tip percentage, and the number of people to split the bill. 
# The tip percentage is divided by 100 and added to 1 to get a multiplier. 
# The total bill is divided by the number of people, and the multiplier is applied to the result. 
# The final amount is rounded to 2 decimal places and formatted as a string with 2 decimal places. 
# The calculated amount is then displayed as a message.

# 두 번째 접근 방식에서는 코드가 다른 방법으로 팁이 포함된 계산을 수행합니다.
# 사용자에게 총 청구액, 팁 비율 및 청구액을 나눌 사람 수를 입력 받습니다.
# 팁 비율은 100으로 나누고 1을 더하여 곱셈 기수를 얻습니다.
# 전체 청구액은 사람 수로 나누고, 곱셈 기수를 결과에 적용합니다.
# 최종 금액은 소수점 이하 2자리로 반올림되고, 2자리로 형식화된 문자열로 변환됩니다.
# 계산된 금액은 메시지로 표시됩니다.
##################################################################################

# Difference between the Approaches
# The main difference between the two approaches lies in how the bill with tip is calculated.
# In the first approach, an f-string is used to calculate the bill with tip by concatenating the tip percentage to a string representation of 1. 
# The resulting value is then multiplied with the bill divided by the number of people.
# In the second approach, the tip percentage is divided by 100 and added to 1 to obtain a multiplier. 
# This multiplier is then applied to the bill divided by the number of people to calculate the bill with tip.
# Both approaches achieve the same result, which is to calculate the amount each person should pay, considering the bill, tip percentage, and the number of people.
# 두 접근 방식의 차이점은 팁이 포함된 청구액을 계산하는 방식에 있습니다.
# 첫 번째 접근 방식에서는 f-문자열을 사용하여 팁이 포함된 청구액을 계산하는데, 팁 비율을 1의 문자열 표현과 연결하여 구합니다.
# 그 결과값은 청구액을 사람 수로 나눈 값에 곱해집니다.
# 두 번째 접근 방식에서는 팁 비율을 100으로 나눈 뒤 1을 더하여 곱셈 기수를 얻습니다.
# 이 곱셈 기수는 청구액을 사람 수로 나눈 값에 적용하여 팁이 포함된 청구액을 계산합니다.
# 두 방식 모두 청구액, 팁 비율 및 사람 수를 고려하여 각 사람이 지불해야 할 금액을 계산하는 동일한 결과를 얻습니다.
##################################################################################
