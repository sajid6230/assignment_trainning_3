'''
9. Write a function to swap the numbers without using a third variable
'''


def swap_numbers(a,b):

    print(f'Given number a = {a} and b = {b}')
    a = a+b
    b = a-b
    a = a-b

    
    print(f'After swap a = {a} and b = {b}')


input1 = int(input('Enter a value for a: '))
input2 = int(input('Enter a value for b: '))
swap_numbers(input1,input2)
