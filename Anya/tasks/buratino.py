dir_ = "u" # u d l r - куда мы смотрим
x = 0
y = 0


while True:
    command = input().lower()

    if command == "шаг":
        if dir_ == "u":
            y += 1
        if dir_ == "d":
            y -= 1
        if dir_ == "l":
            x -= 1
        if dir_ == "r":
            x += 1

    if command == "направо":
        if dir_ == "u":
            dir_ = "r"
        if dir_ == "d":
            dir_ = "l"
        if dir_ == "l":
            dir_ = "u"
        if dir_ == "r":
            dir_ = "d"

    if command == "налево":
        if dir_ == "u":
            dir_ = "l"
        if dir_ == "d":
            dir_ = "r"
        if dir_ == "l":
            dir_ = "d"
        if dir_ == "r":
            dir_ = "u"

print(x, y)