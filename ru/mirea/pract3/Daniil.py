import struct

AS = 1 + 2 + 8 + 8
BS = 2 + 2 + 8 + 1 * 7
DS = 4 + 4 + 2 + 4 + 4 * 5
CS = 4 * 7


def parse_c(offset, bytes):
    c = bytes[offset:offset + CS]
    rez = struct.unpack('<7f', c)
    return {'C1': rez[0], 'C2': list(rez[1:7])}


def parse_d(offset, bytes):
    d = bytes[offset:offset + DS]
    rez = struct.unpack('<IfHf5i', d)
    return {'D1': rez[0], 'D2': rez[1], 'D3': rez[2], 'D4': rez[3], 'D5': list(rez[4:9])}


def parse_b(offset, bytes):
    b = bytes[offset:offset + BS]
    rez = struct.unpack('<HHq7b', b)
    b1_b = bytes[rez[1]:rez[1] + rez[0] * 2]
    b1_r = struct.unpack('<' + 'H' * rez[0], b1_b)
    b1 = [parse_c(addr, bytes) for addr in b1_r]
    return {'B1': b1, 'B2': rez[2], 'B3': list(rez[3:10])}


def parse_a(offset, bytes):
    a1 = parse_b(offset, bytes)
    offset += BS
    a = bytes[offset:offset + AS]
    rez = struct.unpack('<bhQQ', a)
    return {'A1': a1, 'A2': rez[0], 'A3': rez[1], 'A4': rez[2], 'A5': rez[3], 'A6': parse_d(offset + AS, bytes)}


def f31(x):
    return parse_a(4, x)
