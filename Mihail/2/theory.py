def f(x, y, z, w):
    print('x=', x, 'y=', y, 'z=', z, 'w=', w)


params = {
    "w" : 5,
    "x": 0,
    "z" : -1,
    "y": 8
}


f(**params) # kwarg