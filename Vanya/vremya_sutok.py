num = input()

if num.isdecimal():
    num = int(num)
    if num > 5:
        print("utro")
    elif 5 <= num <= 10:
        print("den")
else:
    print("Ошибка")


