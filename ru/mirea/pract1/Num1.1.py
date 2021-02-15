import math

print("Введите числа: ")
x = int(input())
y = int(input())


def fun():
    print("Result: ")
    f = math.cos(pow(x, 8)) - 50 * pow(x, 7) + 90 - (28*pow(x, 3) + 8*pow(x, 7))
    f -= (math.sin(68*pow(x, 5) - abs(y) + 90) + 75*y)
    return f


print('%.2e' % fun())