# Перевод в ЛЮБУЮ СС от 2 до 9

num = 423423

res = '' # str

while num > 0:
    res += str(num%2) # троичная система, поэтому 3
    num //= 2 # троичная система, поэтому 3

res = res[::-1]

print(res)




# Перевод В ЛЮБУЮ СС до 36 ВКЛЮЧИТЕЛЬНО

# from string import digits, ascii_uppercase


# alph = digits + ascii_uppercase

# num = 814569

# res = ''

# while num > 0:
#     res += alph[num%25] #  # 25ричная система, поэтому 25
#     num //= 25

# res = res[::-1]

# print(res)
