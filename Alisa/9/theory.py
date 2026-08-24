#  в строке все числа различны
def check(row: list):
    return (
        len(row) == len(set(row))
    )


# сумма максимального и минимального
# чисел строки больше суммы оставшихся трёх её чисел.

# row = [5, 2, 4, 8, -3]

def check(row: list):
    row = sorted(row)
    return (
        row[0] + row[-1] > sum(row[1:-1])
    )

def check(row: list):
    return (
        max(row) + min(row) > sum(row) - max(row) - min(row)
    )



# среднее арифметическое неповторяющихся
# чисел строки больше её повторяющего (3 раза) числа.
def check(row: list):
    uniq = []
    povtor = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            uniq.append(num)

    return (
        sum(uniq)/len(uniq) > povtor[0]
    )


# в строке все числа расположены в порядке возрастания
# (не путать с неубыванием)
def check(row: list):
    return (
        (row == sorted(row)) and (len(row) == len(set(row)))
    )




def check(row: list):
    return (
        max(row) + min(row) > sum(row) - max(row) - min(row)
    )