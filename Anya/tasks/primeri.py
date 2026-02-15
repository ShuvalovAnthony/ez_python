a = int(input())
b = int(input())
c = int(input())



for left in range(a, b + 1, c):
    for right in range(a, b + 1, c):
        print(left, "+", right, "=", left + right, end="\t")
    print()
