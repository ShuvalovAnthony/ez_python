f = open("Katia/24/69932/69932.txt").read()


res = []

temp_exp = '43276-534550'

for i in range(len(f)):
    curr = f[i]

    if not temp_exp:
        if curr in "0*":
            continue
        else:
            temp_exp += curr
    else:
        if temp_exp[-1] in "*-":
            if curr in "*-0":
                res.append(temp_exp[:-1])
                temp_exp = ""
                continue
            else:
                temp_exp += curr
        elif temp_exp[-1] == "0" and curr in "-*":
            res.append(temp_exp)
            temp_exp = ""
            continue
        else:
            temp_exp += curr


res = sorted(res, key=lambda x: -len(x))


for num in res[:10]:
    print(len(num))

    

