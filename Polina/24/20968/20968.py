from re import findall


f = open("Polina/24/20968/24_20968.txt").read()



num = r"(?:0|[1-9][0-9]*[02468])"
pattern = rf'{num}(?:[+*]{num})*'


words = findall(pattern, f)


print(sorted(words, key=lambda x:len(x), reverse=True)[:10])

# print(max([len(i) for i in words]))


