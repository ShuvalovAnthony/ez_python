f = open("Mihail/24/76127/24_1.txt").read()


valid_exp = []

temp_exp = ''

for i in range(len(f)):
    if not temp_exp:
        if f[i] in "123456789":
            temp_exp += f[i]
        else:
            continue
    else:
        if temp_exp[-1] in "-+":
            if f[i] in "-+":
                valid_exp.append(temp_exp[:-1])
                temp_exp = ''
            else:
                temp_exp += f[i]
        elif temp_exp[-2:] in ("+0", "-0"):
            if f[i] not in "+-":
                valid_exp.append(temp_exp[:-1])
                temp_exp = ''
            else:
                temp_exp += f[i]
        else:
            temp_exp += f[i]

valid_exp = sorted(valid_exp, key=lambda x: -len(x))

print(len(valid_exp[0]), valid_exp[0])

    