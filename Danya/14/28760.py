num = 2*2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561


# counter = 0

# while num > 0:
#     ost = num%27
#     if (ost%2 == 0) and (ost > 9):
#         counter += 1

#     num //= 27


# print(counter)
# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase # - не обязательно!!!

letters = []

while num > 0:
    letters.append(num%27)

    num //= 27

letters = letters[::-1]

letters = [i for i in letters if (i%2 == 0 and i > 9)]

print(len(letters))