from re import findall


f = open("Evgenii/24/20813/24_20813.txt").read()

num = r"(?:0|[7-9][0789]*)"
pattern = rf"{num}(?:[*-]{num})*"


words = findall(pattern, f)

print(max(len(i) for i in words))