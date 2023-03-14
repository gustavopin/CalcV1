x = float; y = float
opperation = str

print('Types of opperation available:')
print()
print('A for Sum')
print('B for Subtraction')
print('C for Multiplication')
print('D for Division')
print()

opperation = input('Hello and welcome to Calc.V1, what type of calculation would you like to do? ')
print()

sum = 0
sub = 0
mult = 0
divi = 0

if opperation == 'A':
    x = float(input('Type the first number: '))
    y = float(input('Type the second number: '))
    sum = x + y
    print(f'Total sum: {sum}')
    n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))
    while n == 'Y':
        x = float(input('Type the next number: '))
        sum = sum + x
        print(f"Total Sum: {sum}")
        n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))

elif opperation == 'B':
    x = float(input('Type the first number: '))
    y = float(input('Type the second number: '))
    sub = x - y
    print(f'Total subtraction: {sub}')
    n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
    while n == 'Y':
        x = float(input('Type the next number: '))
        sub = sub - x
        print(f"Total subtraction: {sub}")
        n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
 
elif opperation == 'C':
    x = float(input('Type the first number: '))
    y = float(input('Type the second number: '))
    mult = x * y
    print(f'Multiplication total: {mult}')
    n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))
    while  n == 'Y':
        x = float(input('Type the next multiplier: '))
        mult = mult * x
        print(f'Multiplication total: {mult}')
        n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))

elif opperation == 'D':
    x = float(input('Type the dividend number: '))
    y = float(input('Type the divisor number: '))
    if y == 0:
        print('The number cannot be divided by zero, try another number!')
        y = float(input('Type the divisor number: '))
    divi = x / y
    print(f'Total division: {divi}')
    n = str(input('Do you want to divide the result of the last opperation (Y/N)? '))
    while  n == 'Y':
        x = float(input('Type the next divisor: '))
        divi = divi / x
        print(f'Total division: {divi}')
        n = str(input('Do you want to divide the result of the last opperation (Y/N)? '))
        
else:
    print('Could not find that on our list, please choose a letter from the options available')