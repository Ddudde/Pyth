import struct

class C32:
    c = True
    s = True
    p = True
    cu = 2
    sw = 0
    pu = 1

    def __init__(self):
        """"""

    def cue(self):
        if self.c:
            if self.cu == 2:
                return 2
            if self.cu == 6:
                self.s = False
                self.c = True
                self.p = True
                self.pu = 5
                return 6
        else:
            raise RuntimeError

    def sway(self):
        if self.s:
            if self.sw == 0:
                self.c = False
                self.sw = 3
                self.pu = 4
                return 0
            if self.sw == 3:
                self.s = False
                self.p = False
                self.c = True
                self.cu = 6
                return 3
            if self.sw == 8:
                self.sw = 9
                return 8
            if self.sw == 9:
                self.s = False
                self.c = False
                return 9
        else:
            raise RuntimeError

    def pull(self):
        if self.p:
            if self.pu == 1:
                self.s = False
                self.p = False
                self.cu = 6
                return 1
            if self.pu == 4:
                self.s = False
                self.p = False
                self.c = False
                return 4
            if self.pu == 5:
                self.pu = 7
                self.c = False
                return 5
            if self.pu == 7:
                self.p = False
                self.s = True
                self.sw = 8
                return 7
        else:
            raise RuntimeError


ES = 3
BS = 4 + 8 + 2 + 4 + 4 + 4 + 4 + 1
CS = 4 + 2 + 4 + 1 + 4 + 4 + 2
DS = 4 + 8 + 8 + 2 + 2


def parse_e(offset, bytes):
    e = bytes[offset:offset + ES]
    rez = struct.unpack('>Bh', e)
    return {'E1': rez[0], 'E2': rez[1]}


def parse_d(offset, bytes):
    d = bytes[offset:offset + DS]
    rez = struct.unpack('>IddHH', d)
    d3_b = bytes[rez[4]:rez[4] + rez[3]]
    d3_r = struct.unpack('b' * rez[3], d3_b)
    return {'D1': rez[0], 'D2': list(rez[1:3]), 'D3': list(d3_r)}


def parse_c(offset, bytes):
    c = bytes[offset:offset + CS]
    rez = struct.unpack('>iHIBIIH', c)
    c2_b = bytes[rez[2]:rez[2] + rez[1]*4]
    c2_r = struct.unpack('>' + 'I' * rez[1], c2_b)
    c2_l = [parse_d(addr, bytes) for addr in c2_r]
    return {'C1': rez[0], 'C2': c2_l, 'C3': rez[3], 'C4': list(rez[4:6]), 'C5': rez[6]}


def parse_b(offset, bytes):
    b = bytes[offset:offset + BS]
    rez = struct.unpack('>iQHIIIfB', b)
    b5_b = bytes[rez[5]:rez[5] + rez[4]]
    b5_r = struct.unpack('b' * rez[4], b5_b)
    return {'B1': rez[0], 'B2': rez[1], 'B3': rez[2], 'B4': parse_c(rez[3], bytes), 'B5': list(b5_r), 'B6': rez[6], 'B7': rez[7]}


def parse_a(offset, bytes):
    a12345 = bytes[offset:offset + 18]
    rez12345 = struct.unpack('>HqHfh', a12345)
    a7 = bytes[offset + 18 + ES: offset + 18 + ES + 1]
    rez7 = struct.unpack('>b', a7)
    return {'A1': parse_b(rez12345[0], bytes), 'A2': rez12345[1], 'A3': rez12345[2], 'A4': rez12345[3], 'A5': rez12345[4], 'A6': parse_e(offset + 18, bytes), 'A7': rez7[0]}


def f31(x):
    return parse_a(4, x)
