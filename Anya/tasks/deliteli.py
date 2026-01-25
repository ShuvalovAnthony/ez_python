num = int(input())

div = 1

while div <= num:
    if num%div == 0:
        print(div)
    div += 1



# divs = set()

# for div in range(1, int(num**0.5) + 1):
#     if num%div == 0:
#         print(div, num//div)