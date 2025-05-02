def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

    return (
        ((len(povtor) == 6) and (len(unique) == 2)) and
        ((max(povtor) - min(povtor))**2 > 2*sum(unique))
    )
