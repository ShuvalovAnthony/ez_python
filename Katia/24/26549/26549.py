f = open("Katia/24/26549/24_26549.txt").read()

f = f.replace("2025", "_")

indexes = []


for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 51):
    left = indexes[i] # ‼️🚨
    right = indexes[i + 51] # ‼️🚨

    substr = f[left + 1: right]

    # print(substr.count("_"), substr[:5], substr[-5:])‼️🚨‼️🚨

    if (substr[-1] == "_") and (substr.count("Y") >= 140): #‼️🚨‼️🚨
        # print(substr.count("_"), substr[:5], substr[-5:]) #‼️🚨‼️🚨
        max_len = max(max_len, len(substr) + 50*3 + 3)

print(max_len)