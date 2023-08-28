# Tip Calculator 팁계산기

This Python project calculates the amount each person should pay, including a tip, based on the total bill, tip percentage, and the number of people splitting the bill.

## Instructions

1. When prompted, enter the total bill amount: "What was the total bill? $".
2. Enter the desired tip percentage: "What percentage tip would you like to give? 10, 12, or 15?".
3. Provide the number of people splitting the bill: "How many people to split the bill?".
4. The program will calculate the amount each person should pay, including the tip, and display the result.

## Example

Let's assume the total bill was $150.00, and you want to split it between 5 people with a 12% tip. Here's how the program would calculate the amount:

```python
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
new_percentage_tip = f"1.{percentage_tip}"
people = int(input("How many people to split the bill? "))
each_pay = (total_bill / people) * float(new_percentage_tip)
print(f"Each person should pay: ${round(each_pay, 2)}")
```

## Code Comparison

The provided code offers an alternative solution for the tip calculator project. Here are the main differences compared to other approaches:

Percentage Calculation:

- Other Approaches: Instead of dividing the tip percentage by 100, the code directly incorporates the tip percentage into the calculation using an f-string. For example, if the tip percentage entered is 12, the line `(total_bill / people) * float(new_percentage_tip)` calculates each person's payment as `(total_bill / people) * 1.12`.

- My Code: My code use an f-string to include the tip percentage directly in the calculation. For example, if the tip percentage entered is 12, the line `(total_bill / people) * float(new_percentage_tip)` calculates each person's payment as `(total_bill / people) * 1.12`.
