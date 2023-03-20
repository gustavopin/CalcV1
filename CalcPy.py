#libraries
import math


#main variables
#x = float; y = float variables for calculations
#operation = str variable for type of operation
# z = str z is the variable to loop the calculator from finish to start

#launcher
z = str(input('Would you like to start the calculator (Y/N) '))
while z == 'Y':

    #table of operations
    print('\nTypes of operation available:')
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
        sum = x + y
        print(f'\nTotal sum: {sum}')
        n = str(input('\nDo you want to sum more numbers to the result of the last opperation (Y/N)? '))
        #continue the sum based on the result of the last operation
        while n == 'Y':
            x = float(input('\nType the next number: '))
            sum = sum + x
            print(f"\nTotal Sum: {sum}")
            n = str(input('\nDo you want to sum more numbers to the result of the last opperation (Y/N)? '))

    #Subtraction operation
    elif operation == 'B':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        sub = x - y
        print(f'\nTotal subtraction: {sub}')
        n = str(input('\nDo you want to subtract more numbers from the result of the last opperation (Y/N)? '))
        #continue the subtraction based on the result of the last operation
        while n == 'Y':
            x = float(input('\nType the next number: '))
            sub = sub - x
            print(f"\nTotal subtraction: {sub}")
            n = str(input('\nDo you want to subtract more numbers from the result of the last opperation (Y/N)? '))

    #Multiplication operation
    elif operation == 'C':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        mult = x * y
        print(f'\nMultiplication total: {mult}')
        n = str(input('\nDo you want to multiply the result of the last opperation (Y/N)? '))
        #continue the multiplication based on the result of the last opperation
        while  n == 'Y':
            x = float(input('\nType the next multiplier: '))
            mult = mult * x
            print(f'\nMultiplication total: {mult}')
            n = str(input('\nDo you want to multiply the result of the last opperation (Y/N)? '))

    #Division Operation
    elif operation == 'D':
        x = float(input('Type the dividend number: '))
        y = float(input('Type the divisor number: '))
        if y == 0:
            print('\nThe number cannot be divided by zero, try another number!')
            y = float(input('\nType the divisor number: '))
        divi = x / y
        print(f'\nTotal division: {divi}')
        n = str(input('\nDo you want to divide the result of the last opperation (Y/N)? '))
        #continue the division based on the result of the last operation
        while  n == 'Y':
            x = float(input('\nType the next divisor: '))
            divi = divi / x
            print(f'\nTotal division: {divi}')
            n = str(input('\nDo you want to divide the result of the last opperation (Y/N)? '))


    #Percentage of a certain number
    elif operation == 'E':
        print('A to know how much is a certain percentage of a number')
        print('B to know the percentage of a number compared to a base number')
        #choice of what percentage operation to do
        n = str(input('\nWhat type of percentage operation do you want to do? '))
        if n == 'A':
            x = float(input('\nType a number: '))
            y = float(input('Type the wanted percentage of the number: '))
            if y < 0:
                print ('\nNegative percentages do not exist, please, type another number')
            else:
                perc = (x / 100) * y
                print(f'\n{y}% of {x} is {perc}')
        
        #rule of three    
        elif n == 'B':
            x = float(input('\nType a base number (it will be your 100%): '))
            y = float(input('Type the second number (it will be compared to the first one): '))
            perc = (y * 100) / x
            print(f'\n{y} is {perc}% of {x}')
        else:
           print('\nOpperation not found.') 

    #Square root operation
    elif operation == 'F':
        x = float(input('\nType the number: ' ))
        while x < 0:
            print('\nThe square root of this number is not possible with simple math')
            x = float(input('\nTry another number: ' ))
        root = math.sqrt(x)
        print(f'\nThe square root of {x} is {root}')

    #exponentiation operation
    elif operation == 'G':
        x = float(input('Type your base number: '))
        y = float(input('Type your exponent: '))
        expo = x ** y
        print(f'\n{x} to the {y} is: {expo}')

    #logarithm operation
    elif operation == 'H':
        x = float(input('Type the number you want to calculate the logarithm from: '))
        if x > 0:
            y = float(input('\nType the base number of the Logarithm function: '))
            log = math.log(x,y)
            print(f'\nThe logarithm of {x} base {y} is {log}')

        else:
            print('\nThe log of negative numbers and zero is UNDEFINED, please try again')
  
    #Message shown if the user type any letter that is not included in the table of operations        
    else:
        print('\nCould not find that on our list, please choose a letter from the options available')

    #loop to start over
    z = str(input('\nWould you like to do another operation (Y/N) '))