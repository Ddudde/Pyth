import math

print("Введите n: ")
n = 14
i = 2


def fun(x1, x2):
    global i
    f = (1 / 67) * pow(x1, 2) - (1 / 90) * pow(x2, 3)
    i += 1
    print(i)
    if i != n:
        fun(x2, f)
    if i == n:
        print('%.2e' % f)


fun(8, 9)
