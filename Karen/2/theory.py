def func(x, y, z):
    print("x=", x, "y=", y, "z=", z)


params = {
    "x" : 7,
    "z" : 15,
    "y" : 11
}


func(**params)