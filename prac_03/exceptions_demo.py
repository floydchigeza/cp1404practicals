"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When entering hello or pi (3.14) due
2. When will a ZeroDivisionError occur? When zero is put as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    denominator = int(input("Please try again, enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
print("Finished.")
