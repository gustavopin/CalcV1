#main variables
x = float; y = float
opperation = str
z = str #z is the variable to loop the calculator from finish to start

#launcher
z = str(input('Would you like to start the calculator (Y/N) '))
while z == 'Y':

    #table of opperations
    print('Types of opperation available:')
    print()
    print('A for Sum')
    print('B for Subtraction')
    print('C for Multiplication')
    print('D for Division')
    print('E for Percentage')
    print()

    #Welcome and first phase of the program. Here it will difine what opperation the user will do
    opperation = input('Hello and welcome to Calc.V1, what type of calculation would you like to do? ')
    print()

    #The variables for the four basic opperations and their initial values
    sum = 0
    sub = 0
    mult = 0
    divi = 0
    perc = 0

    #Sum opperation
    if opperation == 'A':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        print()
        sum = x + y
        print(f'Total sum: {sum}')
        print()
        n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))
        print()
        while n == 'Y':
            x = float(input('Type the next number: '))
            print()
            sum = sum + x
            print(f"Total Sum: {sum}")
            print()

            n = str(input('Do you want to sum more numbers to the result of the last opperation (Y/N)? '))
            print()

    #Subtraction opperation
    elif opperation == 'B':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        print()
        sub = x - y
        print(f'Total subtraction: {sub}')
        print()
        n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
        print()
        while n == 'Y':
            x = float(input('Type the next number: '))
            print()
            sub = sub - x
            print(f"Total subtraction: {sub}")
            print()
            n = str(input('Do you want to subtract more numbers from the result of the last opperation (Y/N)? '))
            print()

    #Multiplication opperation
    elif opperation == 'C':
        x = float(input('Type the first number: '))
        y = float(input('Type the second number: '))
        mult = x * y
        print(f'Multiplication total: {mult}')
        print()
        n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))
        print()
        while  n == 'Y':
            x = float(input('Type the next multiplier: '))
            print()
            mult = mult * x
            print(f'Multiplication total: {mult}')
            print()
            n = str(input('Do you want to multiply the result of the last opperation (Y/N)? '))
            print()

    #Division Opperation
    elif opperation == 'D':
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
        while  n == 'Y':
            x = float(input('Type the next divisor: '))
            divi = divi / x
            print(f'Total division: {divi}')
            print()
            n = str(input('Do you want to divide the result of the last opperation (Y/N)? '))
            print()

    #Percentage of a certain number
    elif opperation == 'E':
        print()
        print('A to know how much is a certain percentage of a number')
        print('B to know the percentage of a number compared to a base number')
        print()
        n = str(input('What type of percentage operation do you want to do? '))
        print()
        if n == 'A':
            x = float(input('Type a number: '))
            y = float(input('Type the wanted percentage of the number: '))
            perc = (x / 100) * y
            print(f'{y}% of {x} is {perc}')
            print()
        elif n == 'B':
            x = float(input('Type a base number (it will be your 100%): '))
            y = float(input('Type the second number (it will be compared to the first one): '))
            perc = (y * 100) / x
            print(f'{y} is {perc}% of {x}')
            print()
        else:
           print('Opperation not found.') 
           print()

    #Message shown if the user type any letter that is not included in the table of opperations        
    else:
        print('Could not find that on our list, please choose a letter from the options available')
        print()

    z = str(input('Would you like to do another operation (Y/N) '))
    print()