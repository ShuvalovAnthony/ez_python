from re import findall

f = open("Vladimir/24/19969/24_19969.txt").read()


pattern = r'(?:[a-z]+@[a-z]+\.[a-z]+)'

words = findall(pattern, f)



# print(words)
print(max([len(i) for i in words]))