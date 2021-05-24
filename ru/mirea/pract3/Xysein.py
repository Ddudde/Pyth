import struct

AS = 8 + 2 + 4 * 5 + 2
BS = 4 + 2 + 4
CS = 1 + 1 + 4
DS = 8 + 8 + 2 + 4 + 8 + 2 + 4


def parse_d(offset, bytes):
    d = bytes[offset:offset + DS]
    rez = struct.unpack('<qqHfQhi', d)
    return {'D1': rez[0], 'D2': rez[1], 'D3': rez[2], 'D4': rez[3], 'D5': rez[4], 'D6': rez[5], 'D7': rez[6]}


def parse_c(offset, bytes):
    c = bytes[offset:offset + CS]
    rez = struct.unpack('<Bbi', c)
    return {'C1': rez[0], 'C2': rez[1], 'C3': rez[2]}


def parse_b(offset, bytes):
    b = bytes[offset:offset + BS]
    rez = struct.unpack('<IHi', b)
    b1_b = bytes[rez[1]:rez[1] + rez[0]]
    b1_r = struct.unpack('c' * rez[0], b1_b)
    b1 = b''.join(list(b1_r)).decode('utf8')
    b3 = [parse_c(offset + BS, bytes), parse_c(offset + BS + CS, bytes)]
    BS_n = BS + 2 * CS
    b = bytes[offset + BS_n:offset + BS_n + 2 + 1 + 1]
    rez4 = struct.unpack('<HbB', b)
    return {'B1': b1, 'B2': rez[2], 'B3': b3, 'B4': rez4[0], 'B5': rez4[1], 'B6': rez4[2]}


def parse_a(offset, bytes):
    a = bytes[offset:offset + AS]
    rez = struct.unpack('<QhIIIIIH', a)
    a4_b = bytes[rez[4]:rez[4] + rez[3]]
    a4_r = struct.unpack('c' * rez[3], a4_b)
    a5_b = bytes[rez[6]:rez[6] + rez[5] * 4]
    a5_r = struct.unpack('I' * rez[5], a5_b)
    return {'A1': rez[0], 'A2': rez[1], 'A3': parse_b(rez[2], bytes), 'A4': b''.join(list(a4_r)).decode('utf8'), 'A5': list(a5_r), 'A6': parse_d(rez[7], bytes)}


def f31(x):
    return parse_a(5, x)
