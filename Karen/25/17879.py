# не лучший, но рабочий вариант
# def m(num: int):
#     delit = set()
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             # i - первый делитель
#             # num//i = второй делитель
#             delit.add(i)
#             delit.add(num//i)

#     if delit:
#         return max(delit) + min(delit)
#     return 0

def m(num: int):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # i - первый делитель
            # num//i = второй делитель
            return i + num//i
    return 0



limit = 5

for num in range(800_001, 10**7):
    res = m(num)

    if res%10 == 4:
        print(num, res)
        limit -= 1

    if limit == 0:
        break




# pycharm community edition