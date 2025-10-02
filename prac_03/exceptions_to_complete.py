"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # this line
        is_finished = True
    except: ValueError
    print("Integer must be a valid number, please enter a valid integer.")
    result = int(input("Enter a valid integer: "))
    is_finished = True

print("Valid result is:", result)