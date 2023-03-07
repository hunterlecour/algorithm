# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable
# the task is to invert the variables, so that the first variable contains the second number, while the first number
# is the second variable

# 0(1)
def swap_two_variables(a: int, b: int):
    print(f"\nBefore swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")


test_a = 500
test_b = 1000
swap_two_variables(test_a, test_b)

# code here
# 0(1)
def swap_two_variables(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")


test_a = 500
test_b = 1000
swap_two_variables(test_a, test_b)

# 0(1)
def swap_two_variables(a: int, b: int):
    print(f"\nBefore swap: a = {a}, b = {b}")
    a = a + b # 500 + 1000 = 1500
    b = a - b # 1500 - 1000 = 500
    a = a - b # 1500 - 500 = 1000
    print(f"After swap: a = {a}, b = {b}")


test_a = 500
test_b = 1000
swap_two_variables(test_a, test_b)

