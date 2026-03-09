def to_5(num):
    res = ''
    while num > 0:
        res += str(num%5)
        num //= 5
    
    return res[::-1]


results = []

for x in range(2, 2026):
    num = 5**2025 + 5**200 - x

    num_v_patirichnoi = to_5(num)
    
    results.append([x, num_v_patirichnoi.count("4")])


results = sorted(results, key=lambda x: (
    -x[1],
    -x[0]
))

for row in results[:10]:
    print(row)

