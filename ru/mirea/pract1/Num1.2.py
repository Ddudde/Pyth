import math

print("Введите x: ")
x = int(input())


def fun():
    print("Result: ")
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


print('%.2e' % fun())