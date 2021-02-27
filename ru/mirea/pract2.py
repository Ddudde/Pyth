def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


def zakl(matr):
    sled = []
    m = len(matr[2])
    for i in range(m):
        dan = matr[2][i].split(';')
        if dan[0] == "true":
            matr[2][i] = "Выполнено"
        else:
            matr[2][i] = "Не выполнено"
        sled.append(str(round(float(dan[1]), 1)))
    matr.append(sled)


def vtor(matr):
    m = len(matr[1])
    for i in range(m):
        matr[1][i] = matr[1][i].split(' ')[1]


def perv(matr):
    m = len(matr[0])
    for i in range(m):
        matr[0][i] = matr[0][i].replace('@', '[at]')


def f21(x):
    return 0


def f22(x):
    fd = int(bin(x), 2)
    fd1 = fd & 0b00001111000000000000000000000000
    fd2 = fd & 0b11110000000000000000000000000000
    fd3 = fd & 0b00000000111111111111111111111111
    fd2 = fd2 >> 4
    fd = fd2 | fd3
    fd1 = fd1 >> 24
    fd = fd << 4
    fd = fd | fd1
    return fd


def f23(tabl):
    tabl = transpose(tabl)
    zakl(tabl)
    vtor(tabl)
    perv(tabl)
    return tabl
