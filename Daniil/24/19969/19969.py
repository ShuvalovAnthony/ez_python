from re import findall

f = open("Daniil/24/19969/24_19969.txt").read()

pat = r'(?:[a-z]+@[a-z]+\.[a-z]+)'
words = findall(pat, f)

print(max([len(i) for i in words]))