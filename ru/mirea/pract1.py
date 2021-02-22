import math


def f11(x, y):
    z = pow(x, 7)
    f = math.cos(pow(x, 8)) - 50 * z + 90 - (28*pow(x, 3) + 8*z) - (math.sin(68*pow(x, 5) - abs(y) + 90) + 75*y)
    return f


def f12(x):
    f = 0
    if x < 29:
        f = 77 * pow(x, 4) + pow(x, 3)
    if 29 <= x < 108:
        f = (math.e ** 2) + math.log(x) + math.log(x)
    if 108 <= x < 189:
        f = x - 17 * pow(x, 7)
    if 189 <= x < 276:
        f = math.cos(math.tan(pow(math.e, x))) + 13 * x
    if x >= 276:
        f = math.log(math.cos(x)) - math.pow(math.e, x) + 82
    return f


def f13(n, m):
    f = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f += pow(j, 6) + (pow(i, 5)/49)
    t = 0
    for i in range(1, n + 1):
        t += pow(i, 2) + math.tan(i)
    f += 64 * t
    return f


def f14(n):
    f = 0
    x = 8
    y = 9
    for i in range(2, n+1):
        f = (1 / 67) * pow(x, 2) - (1 / 90) * pow(y, 3)
        x = y
        y = f
    return f
