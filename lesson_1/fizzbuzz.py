# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz

# code here
# O(n)

a = 4 % 2 # no remainder
b = 5 % 2 # 1 remainder
print(a, b)

# for i in range(1, 101):
#     print(i)
#     if i % 3 == 0:
#         print("fizz")
#     if i % 5 == 0:
#         print("Buzz")
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")


def fizzbuzz(n: int):
    for i in range(1, n+1):
        # print(i)
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        else:
            print(i)
fizzbuzz(100)