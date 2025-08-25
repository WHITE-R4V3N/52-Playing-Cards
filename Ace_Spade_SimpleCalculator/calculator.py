# Author:       Emma Gillespie
# Date:         2025-08-25
# Description:  A simple command line calculator built using python.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(f'Select an option: ')
print(f'1. Add\n2. Subtract\n3. Multiply\n4. Divide')

while True:
    choice = input('Enter choice (1/2/3/4 or quit): ')

    if choice.lower() in ['q', 'quit']:
        exit()
    
    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input('Enter number 1: '))
            b = float(input('Enter number 2: '))
        except:
            print('Please enter numbers only!')

        if choice == '1':
            print(f'{a} + {b} = {add(a, b)}')
        elif choice == '2':
            print(f'{a} - {b} = {subtract(a, b)}')
        elif choice == '3':
            print(f'{a} * {b} = {multiply(a, b)}')
        elif choice == '4':
            print(f'{a} / {b} = {divide(a, b)}')