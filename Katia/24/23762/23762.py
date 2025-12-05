f = open("Katia/24/23762/24_23762.txt").read()


# при этом содержится ровно 80 букв Y.
indexes = []
for i in range(len(f)):
    if f[i] == "Y":
        indexes.append(i)

# НО ЕСЛИ БУДЕТ УСЛОВИЕ при этом содержится ровно 80 раз строка XYZ
# f = f.replace("XYZ", "_")
# indexes = []
# for i in range(len(f)):
#     if f[i] == "_":
#         indexes.append(i)

# И В ОТВЕТЕ НЕ ЗАБЫТЬ УЧЕСТЬ, ЧТО ТЫ СДЕЛАЛ ЗАМЕНУ (в ответе +80*2)


max_len = 0


for i in range(len(indexes) - 81):
    left = indexes[i]
    right = indexes[i + 81]

    substring = f[indexes[i] + 1:indexes[i + 81]]

    # print(substring.count("Y"), substring[:5], substring[-5:])

    if substring.count("2025") >= 90:
        max_len = max(max_len, len(substring))


print(max_len)