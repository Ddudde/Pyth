# [(197554106, 208075691), (959419485, 855197145), (469573281, 533850651), (1493978943, 1355084793), (2084574732, 1946247372), (1910323478, 2111017313), (1472627999, 1550340599), (2225759614, 2326157284)]
# (1910323478, 2111017313) вывелось 2111017320
# (1472627999, 1550340599) вывелось 1550340606
# (2225759614, 2326157284) вывелось 2326157288

fd = int(bin(2225759614), 2)
fd1 = fd & 0b00001111000000000000000000000000
fd2 = fd & 0b11110000000000000000000000000000
fd3 = fd & 0b00000000111111111111111111111111
fd2 = fd2 >> 4
fd = fd2 | fd3
fd1 = fd1 >> 24
fd = fd << 4
fd = fd | fd1
print(fd)
"""
binary = str(bin(1910323478))
print(binary)
prbin = binary.split('b')[0]
numbin = binary.split('b')[1]
numbin = numbin[::-1]
lenn = len(numbin)
if lenn < 24:
    print("No C")
    exit()
print("Have piece C")
c = ""
if lenn > 27:
    c = numbin[24:28]
    numbin = numbin[:24] + numbin[28:]
else:
    c = numbin[24:lenn+1]
    numbin = numbin[:24] + numbin[lenn+1:]
numbin += 'b' + prbin
numbin = numbin[::-1]
c = c[::-1]
print(c)
numbin += c
decimal = int(numbin, 2)
print(decimal)
"""