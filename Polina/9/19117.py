def check(row: list):
    povtor = []
    unique = []

    chet = []
    nechet = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

        if num%2 == 0:
            chet.append(num)
        else:
            nechet.append(num)


    return (
        
        (
            (len(povtor) == 2) and (len(unique) == 3)
        ) or
        (
            (chet and nechet) and
            (sum(chet) >  sum(nechet))
        )
    )