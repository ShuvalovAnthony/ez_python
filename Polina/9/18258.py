def check(row: list):
    sorted_row = sorted(row)

    usl = False
    for num in row:
        if row.count(num) > 1:
            summa_cifr = sum([int(i) for i in str(num)])
            if summa_cifr%2 == 0: usl = True

    return (
        (row == sorted_row) and
        (usl)
    )