from random import randint
from string import digits


pin_code = ""
for i in range(4):
    pin_code += digits[randint(0, 9)]

print(pin_code) # позже закомментировать

# Человек подбирает пароль
# Если он угадал какую-то цифру, сказать что цифра номер N угадана
# Делать так, пока не будут угаданы все 4 цифры

while True:
    print()
    guess = input("Введите пинкод ")

    # твой код
    
