f = open("Karen/24/23762/24_23762.txt").read()

indexes = []

for i in range(len(f)):
    if f[i] == "Y":
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 81):
    left = indexes[i] # индекс левой буквы
    right = indexes[i + 81]# индекс правой буквы

    substring = f[left + 1: right] # срез из ФАЙЛА

    if substring.count("2025") >= 90:
        max_len = max(max_len, len(substring))


print(max_len)