from re import findall


f = open("Evgenii/24/22235/24_22235.txt").read()

num = r"(?:[024568]|[1-9][0-9]*[24568])"

pattern = rf"{num}(?:[+*]{num})*"


nums = findall(pattern, f)

res = []

for num in nums:
    if eval(num) != 0:
        res.append(num)


for num in sorted(res, key=lambda x: -len(x))[:20]:
    print(num)


print(len("0*7809698897142843157015414401872056238305779906839852520627354"))
