print("Введите n: ")
n = int(input())
f = 0
x = 8
y = 9

for i in range(2, n+1):
    f = (1 / 67) * pow(x, 2) - (1 / 90) * pow(y, 3)
    x = y
    y = f
print('%.2e' % f)
