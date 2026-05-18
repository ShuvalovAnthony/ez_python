from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:1]

def to_11(num):
    res = ''
    while num > 0:
        res += alph[num%11]
        num //=11
    return res[::-1]

for x in range(1, 3001):
    exp = 9 * 11**210 + 8 * 11**150 - x 
    exp11 = to_11(exp)
    if exp11.count('0') == 60:
        print(x)