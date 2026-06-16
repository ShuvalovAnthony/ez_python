# res = []

# for treh in range(550, 650):
#     for dva in range(50, 100):
#         res.append([treh - dva, treh, dva])


# res = sorted(res, key=lambda x: (
#     x[0]
# ))


# for row in res[-5:]:
#     print(row)


a = [5, 2, 4]


def test(lst: list):
    lst.sort()


test(a)

print(a)