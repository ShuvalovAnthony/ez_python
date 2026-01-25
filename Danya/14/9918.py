vars = set()

for x in range(10, 67):
    for y in range(67):
        if (
            y < x
        ):
            num1 = 7*67**4 + 3*67**3 + x*67**2 + 1*67 + y
            num2 = 4*x**3 + 9*x**2 + y*x + 6

            res = num1 + num2

            vars.add(res)


print(len(vars))