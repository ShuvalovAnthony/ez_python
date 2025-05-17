s = "0123456789ABCDEF"

# 012345
# 56789ABC
# 13579
# ECA8
# 76543
# BA98
# 0369CF
# E83

#    0123456789

# 01234
# 345
# ABC
# DCBA

print(s[:5])
print(s[3:6])
print(s[-4:-1])
print(s[-1:-5:-1])
print(s[::-1])

# ABOBA

# def isPalindrom(text):
#     for i in range(len(text)//2):
#         if text[i] != text[-i - 1]:
#             return False
#     return True


# def isPalindrom(text):
#     return text == text[::-1]


# print(isPalindrom("ABOBA"))