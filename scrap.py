a = 34560 % 10
print(a)

b = 34560 // 10
print(b)

c = 0 % 3
print(c)


def count_odds_evens(number: int):
    result = []
    original_n = n
    odds_list = []
    evens_list = []
    while n != 0:
        result.append(n % 10) # this will do 125 % 10 which is 5 . this will add 5 into the result variable. after 1 loop it will go result = 5 + (n % 10)
        n = n // 10 # this will do 125 // 10 which is 12 . this will change the n into 12 . This will loop over and over until it turns into 0
    for items in result[0:6]:
        print(f'here are the items : {items}')
        if items % 3 == 0:
            odds_list.append(result)
        if items % 2 == 0:
            evens_list.append(result)

    print(f'List of all digits of {original_n} is : {result}')
    print(f'the number of odds is {len(odds_list)} and evens is {len(evens_list)}')

sum_of_three(34560)