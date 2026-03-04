from re import findall


f = open("Karen/24/20813/24_20813.txt").read()


num = r"(?:0|[789][0789]*)"
pat = rf'{num}(?:[-*]{num})+'

exps = findall(pat, f)
exps = sorted(exps, key=lambda x: -len(x))


for exp in exps[:20]:
    print(exp, len(exp))

