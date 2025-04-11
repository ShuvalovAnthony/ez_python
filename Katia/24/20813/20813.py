from re import findall

f = open("Katia/24/20813/24_20813.txt").read()

num = r"(?:0|[789][0789]*)"

pat = rf'{num}(?:[-*]{num})+'

exps = findall(pat, f)

# print(exps)
# print(max([len(i) for i in exps]))


for exp in exps:
    if eval(exp) == 17:
        print(exp)

