"""
# f(0x0bc66fba) = 0x0c66fbab
# f(0x392f945d) = 0x32f945d9
# f(
# 0b1011110001100110111110111010) =
# 0b1100011001101111101110101011
# f(
# 0b111001001011111001010001011101) =
# 0b110010111110010100010111011001
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
print(c)
numbin += c
decimal = int(numbin, 2)
print(hex(decimal))
"""
ch = "0x392f945d"
decimal = int(ch, 16)
fd = int(bin(decimal), 2)
print(bin(fd))
fd1 = fd & 0b0001111000000000000000000000000
print(bin(fd1))
fd = fd ^ fd1
print((len(bin(fd1)) - 4))
fd1 = fd1 >> (len(bin(fd1)) - 6)
print(bin(fd1))
fd = fd << 4
fd = fd | fd1
print(hex(fd))
#"""