'''
10. Write a function which prints only odd digit numbers from 0 to n, where n is the parameter of the function.
'''


def print_odd_numbers(number):

    for i in range(number+1): 
        is_all_add = True # used a flag 
        for j in str(i): #convert the integer number to string to asscess all the digit
            if int(j) % 2 == 0: #cheak if any digit even 
                is_all_add = False #mark the flag wrong
                break
        if is_all_add:
            
            print(i)


number = int(input('Enter a number: '))
print('Olny odd digit numbers: ')
print_odd_numbers(number)