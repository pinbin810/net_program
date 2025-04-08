import socket
import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer)

def getSrcPort(unpacked):
    return unpacked[0]

def getDstPort(unpacked):
    return unpacked[1]

def getLength(unpacked):
    return unpacked[2]

def getChecksum(unpacked):
    return unpacked[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()

print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)

print(unpacked_udphdr)
print('Source Port:', getSrcPort(unpacked_udphdr))
print('Destination Port:', getDstPort(unpacked_udphdr))
print('Length:', getLength(unpacked_udphdr))
print('Checksum:', getChecksum(unpacked_udphdr))