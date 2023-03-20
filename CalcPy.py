#libraries
import math


#main variables
#x = float; y = float variables for calculations
#operation = str variable for type of operation
# z = str z is the variable to loop the calculator from finish to start

#launcher
z = str(input('Would you like to start the calculator (Y/N) '))
print()
while z == 'Y':

    #table of operations
    print('Types of operation available:')
    print()
    print('A for Sum')
    print('B for Subtraction')
    print('C for Multiplication')
    print('D for Division')
    print('E for Percentage')
    print('F for Square root')
    print('G for Exponentiation')
    print('H for Logarithm')
    print()

    #Welcome and first phase of the program. Here it will difine what operation the user will do
    operation = input('Hello and welcome to CalcPy, what type of calculation would you like to do? ')
    print()

    #The variables for operations and their initial values
    sum = 0
    sub = 0
    mult = 0
    divi = 0
    perc = 0
    root = 0
    expo = 0
    log = 0

    #Sum operation
    if operation == 'A':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        print()
        sum = x + y
        print(f'Total sum: {sum}')
        print()
        n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))
        print()
        #continue the sum based on the result of the last operation
        while n == 'Y':
            x = float(input('Type the next number: '))
            print()
            sum = sum + x
            print(f"Total Sum: {sum}")
            print()

            n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))
            print()

    #Subtraction operation
    elif operation == 'B':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        print()
        sub = x - y
        print(f'Total subtraction: {sub}')
        print()
        n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
        print()
        #continue the subtraction based on the result of the last operation
        while n == 'Y':
            x = float(input('Type the next number: '))
            print()
            sub = sub - x
            print(f"Total subtraction: {sub}")
            print()
            n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
            print()

    #Multiplication operation
    elif operation == 'C':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        mult = x * y
        print(f'Multiplication total: {mult}')
        print()
        n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))
        print()
        #continue the multiplication based on the result of the last opperation
        while  n == 'Y':
            x = float(input('Type the next multiplier: '))
            print()
            mult = mult * x
            print(f'Multiplication total: {mult}')
            print()
            n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))
            print()

    #Division Operation
    elif operation == 'D':
        x = float(input('Type the dividend number: '))
        y = float(input('Type the divisor number: '))
        print()
        if y == 0:
            print('The number cannot be divided by zero, try another number!')
            y = float(input('Type the divisor number: '))
            print()
        divi = x / y
        print(f'Total division: {divi}')
        print()
        n = str(input('Do you want to divide the result of the last opperation (Y/N)? '))
        print()
        #continue the division based on the result of the last operation
        while  n == 'Y':
            x = float(input('Type the next divisor: '))
            divi = divi / x
            print(f'Total division: {divi}')
            print()
            n = str(input('Do you want to divide the result of the last opperation (Y/N)? '))
            print()

    #Percentage of a certain number
    elif operation == 'E':
        print()
        print('A to know how much is a certain percentage of a number')
        print('B to know the percentage of a number compared to a base number')
        print()
        #choice of what percentage operation to do
        n = str(input('What type of percentage operation do you want to do? '))
        print()
        if n == 'A':
            x = float(input('Type a number: '))
            y = float(input('Type the wanted percentage of the number: '))
            if y < 0:
                print ('Negative percentages do not exist, please, type another number')
                print()
            else:
                perc = (x / 100) * y
                print(f'{y}% of {x} is {perc}')
                print()
        
        #rule of three    
        elif n == 'B':
            x = float(input('Type a base number (it will be your 100%): '))
            y = float(input('Type the second number (it will be compared to the first one): '))
            perc = (y * 100) / x
            print(f'{y} is {perc}% of {x}')
            print()
        else:
           print('Opperation not found.') 
           print()

    #Square root operation
    elif operation == 'F':
        x = float(input('Type the number: ' ))
        print()
        while x < 0:
            print('The square root of this number is not possible with simple math')
            print()
            x = float(input('Try another number: ' ))
            print()
        root = math.sqrt(x)
        print(f'The square root of {x} is {root}')
        print()

    #exponentiation operation
    elif operation == 'G':
        x = float(input('Type your base number: '))
        y = float(input('Type your exponent: '))
        print()
        expo = x ** y
        print(f'{x} to the {y} is: {expo}')
        print()

    #logarithm operation
    elif operation == 'H':
        x = float(input('Type the number you want to calculate the logarithm from: '))
        if x > 0:
            y = float(input('Type the base number of the Logarithm function: '))
            print()
            log = math.log(x,y)
            print(f'The logarithm of {x} base {y} is {log}')
            print()
        else:
            print()
            print('The log of negative numbers and zero is UNDEFINED, please try again')
            print()
  
    #Message shown if the user type any letter that is not included in the table of operations        
    else:
        print('Could not find that on our list, please choose a letter from the options available')
        print()

    #loop to start over
    z = str(input('Would you like to do another operation (Y/N) '))
    print()