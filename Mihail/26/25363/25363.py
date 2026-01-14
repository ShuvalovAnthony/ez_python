f = open("Mihail/26/25363/26_25363.txt")

n = int(f.readline())


data = [
    [int(i) for i in row.split()] for row in f
]

data = sorted(data, key=lambda x: (
    min(x)
))

top_rating = []
bot_rating = []


for row in data[:20]:
    left, right = row

    if left < right:
        top_rating.append(row)
        print(row, "TOP")
    else:
        bot_rating.append(row)
        print(row, "BOT")
    
# 667 517
print(len(bot_rating) - 1)

