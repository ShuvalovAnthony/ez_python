# Если переводим ИЗ десятичной в 2,8,16 ричные

# num = 5678

# bin_num = bin(num)[2:]
# oct_num = oct(num)[2:]
# hex_num = hex(num)[2:]



# Если переводим В десятичную

# int(ЧИСЛО_КАК_СТРОКА, ИЗ_КАКОЙ_СС)

# num = '324234' # num КАК СТРОКА!!!!!!!!

# int("324234", 2)


# как найти сумму цифр
# способ 1

num = 4234234

# summa_cifr = 0

# for digit in str(num):
#     summa_cifr += int(digit)

# print(summa_cifr)



# способ 2 (генератор)
# summa_cifr = sum([int(i) for i in str(num)])
# print(summa_cifr)
