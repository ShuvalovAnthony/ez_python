from string import ascii_uppercase

f = open("Katia/24/23381/24_23381.txt").read()

for i in "02468":
    f = f.replace(i, " ")

max_len = 0

for substr in f.split():
    if (
        list(set(substr))[0] in ascii_uppercase
    ):
        max_len = max(max_len, len(substr) + 2)

print(max_len)