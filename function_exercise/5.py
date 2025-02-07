'''
5. Write a function to return the square root of the given number. Hint: use in-built function sqrt.
'''
#use the sqrt function from math python library
from math import sqrt

def square_root(number):
    print(f'The Square root of the {number} is {sqrt(number)}')



#using the function
Enter_number = int(input('Enter a number: '))
square_root(Enter_number)
