f = open("Karen/24/21597/24_21597.txt").read()


for i in "6789":
    f = f.replace(i, " ")

exps = f.split()
exps = sorted(exps, key=lambda x: -len(x))



def check(exp: str):
    for bad in ("--", "-*", "*-", "**"):
        if bad in exp:
            return False
        
    if "*" not in exp:
        nums = exp.split("-")
        for num in nums:
            if num and num[0] == "0" and len(num) > 1:
                    return False
        return True
    else:
        last_star_index = 0
        for i in range(len(exp)):
            if exp[i] == "*":
                last_star_index = i
        
        if ("-" in exp) and (exp.index("-") < last_star_index):
            return False
        
        nums = exp.replace("*", " ").replace("-", " ").split()
        for num in nums:
            if num[0] == "0" and len(num) > 1:
                return False
        return True


def check_vars(exp: str):
    res = []
    for i in range(len(exp)):
        for j in range(i + 1, len(exp)):
            sub = exp[i: j + 1]
            if check(sub):
                res.append(sub)

    res = sorted(res, key=lambda x: -len(x))
    result = res[0]

    while result[0] in "*-":
        result = result[1:]
    
    while result[-1] in "*-":
        result = result[:-1]

    return result
            


# check_vars("1*33*544041*514*532*2-2-34-3021*1*1*1*1*2*3*3*4*2-25430-451-12-12-4431-0-0-0-1-*502-**0*")

max_len = 0

for exp in exps[:50]:
    checked_exp = check_vars(exp)

    max_len = max(max_len, len(checked_exp))

print(max_len)