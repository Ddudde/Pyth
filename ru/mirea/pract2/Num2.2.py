ch = str(input())
decimal = int(ch, 16)
binary = str(bin(decimal))
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
numbin += c
decimal = int(numbin, 2)
print(hex(decimal))
