from re import findall


f = open("Alexander/24/20813/24_20813.txt").read()

num = r"(?:0|[789][0789]*)"
pattern = rf"{num}(?:[-*]{num})*"

strings = findall(pattern, f)



print(max(len(i) for i in strings))
