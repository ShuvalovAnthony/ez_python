# Вводят числа, пока не будет введен 0 (остановка ввода)
# вывести YES если было хотя бы одно четное число, в противном случае - вывести NO


contain_even = False

while True:
    n = int(input())

    if n == 0:
        break

    if n%2 == 0:
        contain_even = True

if contain_even:
    print("YES")
else:
    print("NO")