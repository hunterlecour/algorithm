# 1. Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# code here

def sum(number: int):
    result = 0
    for i in range(1, number + 1):   # range (2, 5 + 1) so we include 5
        result = result + i # result += i (0+1 -> 1+2 -> 3+3 -> 6+4 -> 10 + 5)

    print(f'Sum of {number} is {result}')

sum(5)

# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def maximum(a, b, c):
    number_list = (a, b, c)
    x = max(number_list)
    print(f'the max number from 3 values is {x}')

maximum(124, 21, 32)

# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odd_even(number: int):
    string_number = str(number)
    even_number = 0
    odds_number = 0
    for item in string_number:
        if int(item) % 2 == 0:
            even_number += 1
        else:
            odds_number += 1
    print(f'The count for the odd numbers is {odds_number} and the count of the even numbers is {even_number}')

count_odd_even(34560)





