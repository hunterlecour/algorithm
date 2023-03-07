# Our code generates a random
# three-digit number and has to sum up
# all its digits.
#
# For example, if a number is 349, the
# code has to print the number 16,
# because 3 + 4 + 9 = 16.

# code here
# O(n)
# O(1)

a = 125 / 10
b = 125 // 10

print(f'a is the answer including the remainder: {a}')
print(f'b is the answer excluding the remainder: {b}')

def sum_of_three(n: int):
    result = 0
    original_n = n
    while n != 0:
        print("step")
        result = result + (n % 10) # this will do 125 % 10 which is 5 . this will add 5 into the result variable. after 1 loop it will go result = 5 + (n % 10)
        n = n // 10 # this will do 125 // 10 which is 12 . this will change the n into 12 . This will loop over and over until it turns into 0

    print(f'Sum of all digits {original_n} is the result : {result}')

test = 125 # 1 + 2 + 5 = 8
sum_of_three(125)