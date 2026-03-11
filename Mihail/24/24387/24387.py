f = open(r"Mihail/24/24387/24_24387.txt")
data = f.read()
temp_string = ""
# print(data)
res = []
for i in range(len(data)):

    if len(temp_string) == 0:
        temp_string += data[i]
    else:
        if (int(temp_string[-1]) % 2 == 0) == (int(data[i]) % 2 == 0):
            res.append(temp_string)
            temp_string = data[i]
        else:
            temp_string += data[i]
res = sorted(res, key= lambda x:(
    -sum(int(i) for i in x if i in "13579")
))
print(data.index(res[0]))