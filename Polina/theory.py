# типы данных

# int float - числа
# 321, 4234.324 - целые/вещественные

# 321 = 256 + 64 + 1

# мат действия
# операторы
# + - * 
# / обычное деление всегда в результате дает float
# // - целочисленное деление
# % - остаток от деления
# ** - возведение в степень/вычисление корня n-ой степени
# Остаток от деления всегда будет от 0 до делителя минус 1

# строки - str

s = 'aaaaahello    WORLd!     fsdf234      fsdf09234aaaaaaaaaaaaaa'

# text = 'название книги "война и мир" автор - \'Толстой\''

# print(s.upper())
# print(s.lower())

# print(s.count("hello "))

# print(s.index("h"))

# words = s.split()
# print(words)
# print(len(words))

# print(s.lstrip("a"))

# print(s.replace("a", "_", 1))

# print("1010".zfill(8))




#  A - 10 B - 11 C - 12

# for i in range(len(s)):
#     print(s[i])

# print(list(range(10, 100, 3)))
# s = "0123456789ABC"
            # -4 -3 -2 -1

# 23456
# 89ABC
# 01234567
# CBA
# 13579

# print(s[2:7])
# print(s[8:])
# print(s[:8])
# print(s[-1: -4:-1])
# print(s[1:10:2])

# text = "Hello world!"

# text = text[-1] + text[1:-1] + text[0]

# print(text)



# list - списки/массивы

# nums = [3, 7, 10, 11, 3, 3]

# # print(board[1][3])


# # списковые методы

# nums.append(6)

# print(nums.count(3))
# print(nums)



# nums = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '1', 1, 1]

# print(nums.count("1"))

# nums = [1, 2, 3, -1, -2, -7, 10, 100]

# print(sorted(nums, reverse=True))
# print(sorted(nums)[::-1])

# print(5 + nums.pop())
# print(nums)

# nums = nums[2:]



# ip = "192.168.115.1" # ->

# for i in ip.split("."):
#     if i.count("9") > 0:
#         print(i)

# bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split(".")]

# print(bin_ip)


# f = open("Polina/data.txt")

# data = [
#     [int(i) for i in row.split()] for row in f
# ]

# for a, b, c in data:
#     print(a, b, c)


# set - множество

# text = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a metus quis mauris ultrices mattis. Duis vitae arcu et sapien elementum accumsan. Nulla porttitor, ante ut dictum mollis, diam arcu viverra dui, sit amet consequat tellus erat in libero. Nulla posuere diam orci, in suscipit ipsum imperdiet ut. Curabitur hendrerit metus id nisl tempor aliquet. Cras mattis sapien quis eros cursus, eget convallis purus ornare. Proin rhoncus ante vel ipsum sagittis ullamcorper. Duis eleifend dui nisl, nec pretium purus dictum et. Donec eu tortor viverra, tristique risus a, efficitur nisl. Cras id iaculis metus. In suscipit risus ut odio cursus, at convallis nisl fermentum. Mauris tellus enim, pharetra sed neque sit amet, dictum tempus lectus. Suspendisse mattis odio sed aliquet aliquet. Maecenas ligula leo, aliquam in tincidunt nec, aliquet id purus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed mattis blandit mollis.

# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus porttitor ex eu felis laoreet hendrerit. Sed molestie orci ex, id ultricies velit sagittis vitae. Pellentesque ac risus sed nisl iaculis dignissim porttitor eget lacus. Aliquam erat volutpat. Donec finibus iaculis lacinia. Aenean tristique ligula id ultricies commodo. Mauris maximus sem nec nisi dapibus mollis. Cras sed est ac tortor aliquam dignissim. Nunc efficitur nunc id porta blandit. Suspendisse non neque libero. Nulla id dolor enim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Morbi porta urna magna, laoreet pretium quam rhoncus vitae. Morbi massa odio, sagittis sit amet felis nec, fermentum pulvinar odio.

# Vivamus viverra quam tellus, at consectetur purus dictum quis. Aliquam sit amet lorem diam. Curabitur eget urna rutrum lectus pharetra auctor. Aliquam id tellus vel velit mattis consequat. Nulla vitae sem eu nulla porttitor elementum vel sed elit. Maecenas dictum elementum massa. Duis arcu velit, sodales non rhoncus a, dictum non tortor. Aenean vitae quam magna. Fusce et ligula magna. Etiam luctus diam ut orci efficitur fermentum.

# Ut a vestibulum mauris, eu commodo magna. Duis cursus odio metus, eget elementum mi dictum sit amet. Suspendisse viverra mauris et elementum semper. Duis et metus in justo faucibus efficitur. Fusce consectetur accumsan ex quis sodales. Nullam vitae purus eleifend, ullamcorper ante in, suscipit mauris. Praesent laoreet varius lectus. Integer ultrices dui lacus, vel gravida arcu mollis et. Aenean at elementum metus, a facilisis ligula. Praesent hendrerit augue risus, at scelerisque dui sagittis sed. Vestibulum vel facilisis purus."""


# for symb in set(text):
#     print(symb, text.count(symb))


# 65
# 2
# 3
# 4
# 5

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True


# 10**9 do 10**15


# простые оканчиваются на 0 и делятся на 7 без остатка 


# for n in range(10**3, 10**15):
#     if  (n%10 == 3) and isPrime(n):
#         print(n)


# def allDivs(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n%i == 0:
#             divs.add(i)
#             divs.add(n//i)
#     return True


# 10**12 -> 10**6 ~ 10**12
# 1 000 000 000 000
# 1 000 000


# for n in range(10**9, 10**12):
#     print(isPrime(n))



# mnozh = {1, 2, 17, 10, 4, 5, 96, 95, 94}

# # mnozh.add(7)

# # print(mnozh)


# for i in range(20):
#     mnozh.add(i)


# print(sorted(mnozh))


# nums = set()

# print(type(nums))

# tuple - кортежи - неизменяемые списки

# nums = (1, 2, 3, 4)

# nums[-1] = 6

# print(nums[0])
# print(nums[2:])

# nums = (5, )

# print(nums, type(nums))


# students = {
#     "Ivan" : {
#         "city": "fsdgf",
#         "id": 123
#     },
#     "Ivan2" : {
#         "city": "asasf",
#         "id": 213
#     },
#     "Ivan3" : {
        
#         "id": 1233,
#         "city": "grtgrtg",
#     },

# }

# for name, data in students.items():
#     print(name, students[name]["city"])



# from string import digits, punctuation, ascii_uppercase
# from collections import Counter

# text = "242385072485340534534572345923745723452345"

# alph = digits + ascii_uppercase[:8]

# for x in alph:
#     print(x)


# print(Counter(text).most_common(1))



# if elif else - условная конструкция


# дают число, сказать положительное/отриц или 0


# 70 do 100 na 3


# n = 50

# if n < 70:
#     print("error")
# if n < 80:
#     print("1")
# if n < 90:
#     print("2")
# if n < 100:
#     print("3")
# else:
#     print("error")


text = "Fdsg9saagjdfeeeg"

# print(any([i for i in "aeyuio" if i in text]))


# False ==  0 "" [] () {} set() 
# True 234234, -435, " ", 'fdsg'

# if sum([text.lower().count(i) for i in "aeyuio"]) and (len(text) > 5):
#     print("YES")


# for n in range(10):
#     print("YES" if n%2 == 0 else "NO")
