# from string import digits, ascii_uppercase

# alph = digits + ascii_uppercase


# num = 737731173871

# digits = ""

# while num > 0:
#     digits = digits + alph[num%15]
#     num = num//15
# # ABC4345DEF
# print(digits[::-1])



# eggs = int(input())

# while eggs > 0:
#     last_digit = eggs%12
#     eggs = eggs//12


# print(last_digit)

first_max = -1000
second_max = -1000
while True:
    num = int(input())
    if abs(num) > 1000:
        break
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max:
        second_max = num
print(second_max)