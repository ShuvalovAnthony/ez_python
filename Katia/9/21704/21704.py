f = open("Katia/9/21704/21704.txt")


# двумерный список
data = [
    # перевести в инт каждое число из строки
    [int(i) for i in row.split()] for row in f # для каждой строки в файле
]


def check(row):
    sort_row = sorted(row, reverse=True)

    return (
        (row == sort_row) and
        ((sort_row[-1] + sort_row[0])/2 > sum(sort_row[1:-1])/5)
    )



for row in data: # для каждой строки
    if check(row): # проверяем эту строку на валидность в функции
        print(sum(row)) # если ок - пишем сумму чисел в строке
        break # ТК НАИМ НОМЕР - break