from re import findall


f = open("Vladimir/24/19751/24_19751.txt").read()


pat = r'(?:A[1-9]+(?:[+][1-9]+)*)'


res = findall(pat, f)
print(res)
max_sum = 0

for s in res:
    if s[1:]:
        max_sum = max(max_sum, eval(s[1:]))


print(max_sum)