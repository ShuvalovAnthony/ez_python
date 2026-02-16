def check(row: list):
    row = sorted(row) # [1, 2, 3, 4, 5]

    k = 0
    for num in row:
        if str(num)[-1] == "5":
            k += 1


    return (
        (sum(row[-2:])*2 > sum(row[:3])*3) and
        k >= 2
    )