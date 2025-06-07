from itertools import permutations


def algo(s:str):
    while '00' not in s:
        s = s.replace('011', '20')
        s = s.replace('022', '10')
        s = s.replace('02', '110')
        s = s.replace('01', '220')
    return s


# for i in range(46, 47):
#     for p in permutations('12'*i):
#         p = ''.join(p)
#         p = '0' + p + '0'
#         res = algo(p)

#         print(p, res.count('1'), res.count('2'))



for i in range(100):
    s = '0' + '12'*i +'0'

    s = algo(s)

    if s.count('1') == 47:
        print(s.count('2'), i)
    else:
        print(s.count('1'))