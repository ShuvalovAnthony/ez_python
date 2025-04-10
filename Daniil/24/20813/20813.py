from re import findall

f = open("Daniil/24/20813/24_20813.txt").read()

# 0*4234-4234*0-4234*423*0432

pat = r'(?:0|[789][0789]*(?:[*-](?:0|[789][0789]*))+)'

exps = findall(pat, f)


print(max([len(i) for i in exps]))
