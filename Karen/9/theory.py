# в строке все числа различны

# len(set(row)) == len(row)



# в строке есть два числа, каждое из которых 
# повторяется дважды, остальные три числа различны;

# len(povtor) == 4 and len(uniq) == 3



# - в строке все числа расположены в порядке убывания;
# sorted_row = sorted(row, reverse=True)
# row == sorted_row



# среднее арифметическое
# sum(row)/len(row)


# максимальное число не повторяется;
# max(row) not in uniq



# хотя бы половина чисел строки являются трёхзначными числами;
# (в каждой строке шесть натуральных чисел)
# k = 0
# for num in row:
#     if 100 <= num <= 999:
#         k += 1

# k >= 3

# или через генератор
# len([i for i in row if 100 <= i <= 999]) >= 3






# обязательно 1 число повторяется трижды
# обязательно 1 число повторяется дважды
# обязательно 3 числа уникальных


def check(row: list):
    povtor_2 = []
    povtor_3 = []
    uniq = []


    for num in row:
        if row.count(num) == 3:
            povtor_3.append(num)
        if row.count(num) == 2:
            povtor_2.append(num)
        if row.count(num) == 1:
            uniq.append(num)

    return (
        (len(povtor_3) == 3) and
        (len(povtor_2) == 2) and
        (len(uniq) == 3)
    )


row = [15, 8, 14, 15, 15, 9, 3, 8]

print(check(row))
