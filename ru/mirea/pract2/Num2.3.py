class Chel:

    def __init__(self, email, fio, dannye):
        self.email = "None"
        self.fio = "None"
        self.dannye = "None"
        if email:
            self.email = email
        if fio:
            self.fio = fio
        if dannye:
            self.dannye = dannye

    def __repr__(self):
        return self.email + " | " + self.fio + " | " + self.dannye


class TChel:

    def __init__(self, mas):
        self.mas = mas

    def __repr__(self):
        str = self.mas[0]
        for i in range(1, len(self.mas)):
            str += " | " + self.mas[i]
        return str


print("Введите стоп слово(оно не должно встречаться в таблице): ")
stop = str(input())
tabl = []
while True:
    ch = str(input())
    if ch == stop:
        break
    ch = ch.split(" | ")
    chel = Chel(ch[0], ch[1], ch[2])
    tabl.append(chel)
print("Исходная таблица: ")
print(tabl.__repr__()[1:-1].replace(', ', '\n'))
print("\nРезультат преобразования: ")
tabl1 = []
mase = []
masf = []
masb = []
masc = []
for ch in tabl:
    mase.append(ch.email.replace('@', '[at]'))
    masf.append(ch.fio)
    dan = ch.dannye.split(';')
    if dan[0] == "true":
        masb.append("Выполнено")
    else:
        masb.append("Не выполнено")
    masc.append(str(round(float(dan[1]), 1)))
tabl1.append(TChel(mase))
tabl1.append(TChel(masf))
tabl1.append(TChel(masb))
tabl1.append(TChel(masc))
print(tabl1.__repr__()[1:-1].replace(', ', '\n'))
# sudadman40@mail.ru |  | true;0.21
"""
tq
sudadman40@mail.ru | Вадим Шудадман | true;0.21
odissej89@rambler.ru | Одиссей Фагикин | true;0.62
netezin5@yahoo.com | Петр Нетецин | true;0.72
tq

tq
dovezko90@gmail.com | Самир Довезко | false;0.87
samir56@rambler.ru | Самир Читли | false;0.91
kirill82@rambler.ru | Кирилл Тишянц | true;0.20
semen68@yahoo.com | Семен Гечий | true;0.23
tq
"""
