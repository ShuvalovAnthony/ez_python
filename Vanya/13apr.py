# n = int(input())
# m = int(input())

# for i in range(n, m + 1):
#     d1, d2, d3, d4 = i//1000, i//100%10, i//10%10, i%10

#     if (d1 != d2) and (d1 != d3) and (d1 != d4) and (d2 != d3) and (d2 != d4) and (d3 != d4):
#         print(i, d1, d2, d3, d4)


from string import ascii_letters


for letter in ascii_letters:
    print(letter, ord(letter))

