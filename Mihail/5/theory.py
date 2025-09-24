# перевод ИЗ ДЕСЯТИЧНОЙ В:
# 1) двоичная bin()[2:]
# 2) восьмиричная oct()[2:]
# 3) 16тиричная hex()[2:]


# перевод ИЗ любой в 10ую
# int("STROKA!!!!!!!", FROM_BASE)


# Если переводим в СС отличную от 2 8 16
# то пишем функцию САМИ!!!!

def to_5(num):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]



# сумма цифр в числе
# 1) если число int

# num = 5647423
# summa_cifr = sum([int(i) for i in str(num)])

# # 2) если число как строка str

# num = "5647423"
# summa_cifr = sum([int(i) for i in num])



# Если ищем в ответу min N
# то print(n) + break

# Если ищем в ответу max N
# то print(n) - и последнее что напишет


# Если ищем max/min r - делаем ДО ЦИКЛА
# список всех результатов
# добавляем нужные r
# в конце print(max(res)) либо print(min(res))