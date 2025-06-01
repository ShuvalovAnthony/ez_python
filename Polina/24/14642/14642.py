f = open("Polina/24/14642/24.3_14642.txt").read()

words = f.split("F")

max_len = 0

for i in range(len(words) - 1):
    left = words[i]
    right = words[i + 1]

    max_len = max(max_len, len(left) + len(right) + 1)

print(max_len)