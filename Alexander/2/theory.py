from itertools import permutations

# def f(x, y, z, w):
#     print('x', x, 'y', y, 'z', z, 'w', w)



# for p in permutations('xyzw'):
#     params = dict(zip(p, [1, 2, 3, 4]))
#     print(params)
#     f(x=1, y=2, z=3, w=4)
#     print()


def test(a, b, c):
    print(a, b, c)



test(*[1, 2, 3])


