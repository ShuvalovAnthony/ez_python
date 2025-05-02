def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

    return (
        povtor and unique and
        (max(row) not in povtor) and
        (sum(unique) >= sum(povtor)*3)
    )
    