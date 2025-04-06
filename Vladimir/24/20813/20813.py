from re import findall


f = open("Vladimir/24/20813/24_20813.txt").read()


pattern = r'(?:0|[789][7890]+)' + r'(?:[-*](?:0|[789][7890]*))+'


words = findall(pattern, f)

# print(words)
print(max([len(i) for i in words]))