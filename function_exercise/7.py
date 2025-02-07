'''
7. Write a function to print whether a given number is odd or even.
'''
#create a function to check a number is odd or even
def check_odd_even(number):

    if (number%2 == 0):
        print(f'{number} is an Even number')
    else:
        print(f'{number} is an Odd number')


#calling the function
number = int(input('Enter a number: '))
check_odd_even(number)