import struct

AS = 8 + 4 * 4 + 2 + 1 * 7 + 8 + 1 * 8 + 2 * 2 + 2 + 2
BS = 2 + 2 + 1
CS = 1 + 4 + 4
DS = 4 + 4 + 2 + 4 + 4 + 8 + 1 + 8


def parse_d(offset, bytes):
    d = bytes[offset:offset + DS]
    rez = struct.unpack('>fIHfidBd', d)
    return {'D1': rez[0], 'D2': rez[1], 'D3': rez[2], 'D4': rez[3], 'D5': rez[4], 'D6': rez[5], 'D7': rez[6], 'D8': rez[7]}


def parse_c(offset, bytes):
    c = bytes[offset:offset + CS]
    rez = struct.unpack('>Bif', c)
    return {'C1': rez[0], 'C2': rez[1], 'C3': rez[2]}


def parse_b(offset, bytes):
    b = bytes[offset:offset + BS]
    rez = struct.unpack('>Hhb', b)
    return {'B1': parse_c(rez[0], bytes), 'B2': rez[1], 'B3': rez[2]}


def parse_a(offset, bytes):
    a = bytes[offset:offset + AS]
    rez = struct.unpack('>Q4IH7cQ8c2HHH', a)
    a2_l = [parse_b(addr, bytes) for addr in rez[1:5]]
    a4 = b''.join(list(rez[6:13])).decode('utf8')
    a6 = b''.join(list(rez[14:22])).decode('utf8')
    a8_b = bytes[rez[25]:rez[25] + rez[24] * 2]
    a8_r = struct.unpack('>' + 'h' * rez[24], a8_b)
    return {'A1': rez[0], 'A2': a2_l, 'A3': parse_d(rez[5], bytes), 'A4': a4, 'A5': rez[13], 'A6': a6, 'A7': list(rez[22:24]), 'A8': list(a8_r)}


def f31(x):
    return parse_a(4, x)