from string import digits, ascii_uppercase

# алфавит 18ти ричной системы - 10 цифр + первые 8 букв
alph = digits + ascii_uppercase[:8]

# перебираем все возможные x
for x in alph:
    # составляем выражение из задачи
    num = (
        int("11h" + x + "05", 18) +
        int(f"3f{x}54{x}8", 18) +
        int(f"g{x}{x}{x}9", 18)
    )

    if num%14 == 0:
        print(num//14) # внимательно смотрим условие!!!!
        break