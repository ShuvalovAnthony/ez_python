# 564 444

f = open("Vladimir/26/23765/26_23765.txt")

# хранения годности

data = [[int(i) for i in row.split()] for row in f]

data = sorted(data, key= lambda x: min(x))

top_rate = []
bot_rate = []


for row in data:
    if row[0] < row[1]:
        top_rate.append(row)
        print("top", row)
    else:
        bot_rate.append(row)
        print("bot", row)

print(len(bot_rate) - 1)