from re import findall

f = open("Katia/24/19969/24_19969.txt").read()


pat = r'([a-z]+@[a-z]+[.][a-z]+)'

words = findall(pat, f)

# print(words)

print(max([len(i) for i in words]))