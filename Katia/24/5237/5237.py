f = open("Katia/24/5237/24_5237.txt").read()

words = f.split("Z")


def check(stroka: str):
    for i in range(1, len(stroka)):
        if stroka[i] == stroka[i - 1]:
            return False
    return True


max_len = 0

for word in words:
    if check(word):
        max_len = max(max_len, len(word))

print(max_len)
    