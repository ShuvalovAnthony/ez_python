from string import digits, ascii_uppercase

f = open("Daniil/24/21421/24_21421.txt").read()

alph = digits + ascii_uppercase[:2]


for letter in set(f):
    if letter not in alph:
        f = f.replace(letter, ' ')


# sposob 1
max_len = 0
res = ''
for word in f.split():
    word = word.lstrip('0')
    if word:
        num = int(word, 12)
        if (len(word) > max_len) and num%2 == 0:
            max_len = len(word)
            res = word

print(max_len, res)


# sposob2

# def to_12(n):
#     res = ''
#     while n > 0:
#         res += alph[n%12]
#         n //= 12
#     return res[::-1]

# max_len = 0
# for word in f.split():
#     num = int(word, 12)
#     num_in_12 = to_12(num)
#     if len(num_in_12) > max_len and num%2 == 0:
#         max_len = len(num_in_12)

# print(max_len)



# def delete_left_0(substring):
#     for i in substring:
#         if i == '0':
#             substring = substring[1:]
#         else:
#             return substring
#     return '0'

# print(delete_left_0('0000001242342340000000423423400000'))