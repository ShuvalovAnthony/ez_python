from string import digits, ascii_uppercase

alph = digits+ascii_uppercase[:14]
num = 14**1402+28**501-14**51-1400

def chet(num):
    s = ''
    while num>0:
        s += alph[num%14]
        num//=14
    return s[::-1]

c = chet(num)
print(c.count('C'))