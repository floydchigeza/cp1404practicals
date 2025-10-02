""""""


#1 Ask for the users name and write into name.txt
out_file = open("name.txt", "w")
name = input("Enter your name: ")
out_file.write(name)
out_file.close()

#2 In the same file make the response say Hi users name
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
out_file = open("name.txt", "a")
out_file.write(f"\n Hi {name}!")
out_file.close()

print(f"Hi {name}!")

#3 read for numbers.txt and add the first two lines together
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(f"Sum of the first two numbers is: {number1 + number2}")

#4  print the total for all lines in numbers.txt.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(f"Your total is: {total}")