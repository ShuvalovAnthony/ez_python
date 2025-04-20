from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:11]



for x in alph:
    res = (
        int(f'82934{x}2', 21) +
        int(f'2924{x}{x}7', 21) +
        int(f'67564{x}8', 21)
    )

    if res%20 == 0:
        print(res//20)
        break