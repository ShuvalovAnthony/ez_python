from re import findall


f = open("Evgenii/24/19969/24_19969.txt").read()


pattern = r"[a-z]+@[a-z]+[.][a-z]+"


words = findall(pattern, f)

words = sorted(words, key=lambda x: len(x), reverse=True)

print(words[0])