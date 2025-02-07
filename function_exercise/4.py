"""
4. Write a function to accept the number of rows for the pattern and print that many number of rows.

Sample output:

Enter number of rows: 5

*****

****

***

**

*
"""

def print_stars(number):
    for i in range(number,0,-1):
        print(i * '*')


# Calling the function
number_of_rows = int(input("Enter number of rows: "))
print_stars(number_of_rows)