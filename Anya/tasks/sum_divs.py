
# 1 и само число - называются тривиальными делителями
# число 1 - не является простым

# # простой перебор
# num = int(input())
# for delitel in range(1, num + 1):
#     if num%delitel == 0:
#         print(delitel, "является делителем", num)


num = int(input())
deliteli = set()
for i in range(1, int(num**0.5) + 1):
    if num%i == 0:
        print(i, num//i)
        deliteli.add(i)
        deliteli.add(num//i)

print(sum(deliteli))