from re import findall


f = open("Daniil/24/22235/24_22235.txt").read()


num = r'(?:0|[1-9][0-9]*[24568])'
pattern = rf'{num}(?:[+*]{num})*'

exprs = findall(pattern, f)
exprs = sorted(exprs, key= lambda x: len(x), reverse=True)

max_len = 0


def check(exp: str):
    parts_res = []
    if "+" in exp:
        parts = exp.split("+")
        for part in parts:
            parts_res.append([eval(part), len(part)])

    max_len = 0
    temp_len = 0

    for i in range(len(parts_res)):
        if parts_res[i][0] == 0:
            temp_len += parts_res[i][1]
        else:
            max_len = max(max_len, temp_len)
            temp_len = 0
    
    return max(max_len, temp_len)



for exp in exprs:
    if (len(exp) > 50) and (eval(exp) == 0):
        max_len = max(max_len, len(exp))
    elif (len(exp) > 83):
        print(exp, (check(exp)))
        pmax_len = max(max_len, check(exp))


print(max_len)


