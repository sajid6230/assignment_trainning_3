'''
3. Write a function to accept a list of numbers and print the sum of the numbers which follows the below condition:

a. Using sum function

b. Without using sum function

'''
#Using sum function
def with_sum_func(numbers):
    print(f"Sum of numbers: {sum(numbers)}")



#Without using sum function
def without_sum_func(numbers):
    count = 0
    for i in numbers:
        count = count + i
    print(f'Sum of numbers: {count}')


#calling the 1st function 
with_sum_func([2,3,4])

##calling the 2nd function 
without_sum_func([2,3,4,1])