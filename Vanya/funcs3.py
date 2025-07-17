def findHipo(a, b):
    return (a**2 + b**2)**0.5


def isTriangleRight(a, b, c):
    a, b, c = sorted([a, b, c])
    return c**2 == a**2 + b**2




while True:
    a = int(input("Введите первую сторону "))
    b = int(input("Введите вторую сторону "))
    c = int(input("Введите третюю сторону "))

    if isTriangleRight(a, b, c):
        print("Прямоугольный")
    else:
        print("Не прямоугольный")
