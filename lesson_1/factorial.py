# When user enters a number, its factorial is displayed


#code here
# O(n)

def factorial(number: int):
    result = 1
    for i in range(2, number + 1):   # range (2, 5 + 1) so we include 5
        result = result * i # result *= i (1*2 -> 2*3 -> 6*4 -> 24*5)

    print(f'Factorial of {number} is {result}')

factorial(5)
