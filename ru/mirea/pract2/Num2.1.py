rez = -1
f = [1973, 'http', 'dylan', 'forth', 1997]
if f[2] == 'dylan':
    rez = 9
if f[2] == 'tcsh':
    rez = 10
if (f[3] == 'arc') & (rez == -1):
    rez = 11
if rez == -1:
    if f[0] == 2001:
        if f[4] == 2000:
            rez = 0
        if f[4] == 1997:
            rez = 1
        if f[4] == 1965:
            rez = 2
    if f[0] == 1973:
        if f[4] == 2000:
            rez = 3
        if f[4] == 1997:
            rez = 4
        if f[4] == 1965:
            rez = 5
    if f[0] == 1995:
        if f[4] == 2000:
            rez = 6
        if f[4] == 1997:
            rez = 7
        if f[4] == 1965:
            rez = 8
print(rez)
