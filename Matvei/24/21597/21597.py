from re import findall


f = open("Matvei/24/21597/24_21597.txt").read()

num = r'(?:0|[1-5][0-5]*)'
pattern = rf'{num}(?:[*]{num})*(?:[-]{num})*'

words = findall(pattern, f)



words = sorted(words, key= lambda x: len(x), reverse=True)


print(words[0]) # ctrl + f в файле + 5 символов слева

# answer = 51
