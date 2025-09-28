for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print( i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars =int(input("number of stars is:"))
for i in range(number_of_stars):
    print('*',end='')
print()

number_of_rows = int(input("Enter number of rows"))
for i in range(1,number_of_rows + 1,1):
    print('*' * i)