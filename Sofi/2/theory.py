

def f(x, y, z, w):
    print(x, y, z, w)



f(y=5, z=6, x=1, w=2)

params = {
    "y": 5,
    "z": 6,
    "x": 1,
    "w": 2
}

f(**params)