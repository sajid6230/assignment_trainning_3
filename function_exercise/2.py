"""
2. Write a function to print the tables of a given number till 10.

Sample output:

Enter number: 3

3 x 1 = 3

3 x 2 = 6

3 x 3 = 9

.

.

.

3 x 10 = 30
"""
#define the function
def multiple_by_10():
    number = int(input('Enter a number: '))


    for i in range(1,11):
        multiple = i * number
        print(number, 'X' , i, '=',multiple)
    

#call the function
multiple_by_10()
