"""
tabl = [["sudadman40@mail.ru", "Вадим Шудадман", "true;0.21"],
["odissej89@rambler.ru", "Одиссей Фагикин", "true;0.62"],
["netezin5@yahoo.com", "Петр Нетецин", "true;0.72"]]

tabl = [["dovezko90@gmail.com", "Самир Довезко", "false;0.87"],
["samir56@rambler.ru", "Самир Читли", "false;0.91"],
["kirill82@rambler.ru", "Кирилл Тишянц", "true;0.20"],
["semen68@yahoo.com", "Семен Гечий", "true;0.23"]]
"""


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

tabl = [["sudadman40@mail.ru", "Вадим Шудадман", "true;0.21"],
["odissej89@rambler.ru", "Одиссей Фагикин", "true;0.62"],
["netezin5@yahoo.com", "Петр Нетецин", "true;0.72"]]
tabl = transpose(tabl)
zakl(tabl)
vtor(tabl)
perv(tabl)
