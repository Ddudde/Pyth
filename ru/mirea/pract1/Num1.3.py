import math

print("Введите n: ")
n = int(input())
print("Введите m: ")
m = int(input())


def fun():
    print("Result: ")
    f = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f += pow(j, 6) + (pow(i, 5)/49)
    t = 0
    for i in range(1, n + 1):
        t += pow(i, 2) + math.tan(i)
    f += 64 * t
    return f


print('%.2e' % fun())