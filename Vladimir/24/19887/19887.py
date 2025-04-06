from re import findall


f = open("Vladimir/24/19887/24.23_19887.txt").read()


pat = r'(?:[02468][13579]){2,}'
pat2 = r'(?:[13579][02468]){2,}'


res = findall(pat2, f)
print(res)
print(max([len(i) for i in res]))