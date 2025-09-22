from math import sin, cos, radians

g = 9.81
h = 30
for v0 in range(1, 10**4):
    v0 = v0/1000

    t1 = v0*0.5/g
    t2 = ((0.25*v0**2 + 2*g*h) - v0/2)/2
    t = t1 + t2
    if (
        (h - 0.5*v0*t2 - 0.5*g*t2**2 <= 0.1) and
        (
            (v0/2*3**0.5*t) == 2.78*t + 0.25*t**2
        )
    ):
        print(t1 + t2, v0)
