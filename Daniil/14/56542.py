from string import digits, ascii_uppercase
from itertools import product


alph = digits + ascii_uppercase


for p, x, y in product(range(36), alph, alph):
    try:
        left = int(f"{x}{x}{x}8", p) + int(f"43{x}9", p)
        right = int(f"{y}{y}04", p)

        if left == right:
            print(int(f"{y}{y}{x}", p))
    except:
        ...
