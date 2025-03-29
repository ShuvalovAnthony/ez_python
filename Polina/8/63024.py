# from itertools import product


# chet = "2468"
# nechet = "1357"


# def check(num:str):
#     for digit in set(num):
#         if num.count(digit) > 4: 
#             return False
#     return True

# counter = 0

# for num in product(chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet):
#     num = ''.join(num)

#     if check(num):
#         counter += 1


# print(counter * 2)




def check(n):
    n = str(n)

    for i in "2468":
        n = n.replace(i, '0')
    
    for i in "3579":
        n = n.replace(i, '1')

    return ('00' not in n) and ('11' not in n)



