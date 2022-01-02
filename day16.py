import math
from typing import List


# BEGIN: DATAMODEL
class Packet:
    def __init__(self, version):
        self.version = version


class Literal(Packet):
    def __init__(self, version: int, value: int):
        super().__init__(version)
        self.value = value

    def get_value(self) -> int:
        return self.value


class Expression(Packet):
    def __init__(self, version: int, type_id: int, sub_packets: List[Packet]):
        super().__init__(version)
        self.type_id = type_id
        self.sub_packets = sub_packets

    def get_value(self) -> int:
        # TODO: implement value here
        raise ValueError("Not yet implemented")


# END: DATAMODEL


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read()  # .splitlines()

    return content


def read_literal(input_package) -> (int, int):
    literal_value = ""
    package_length = 0

    while input_package[package_length] != '0':
        literal_value += input_package[(package_length + 1): package_length + 5]
        package_length += 5

    literal_value += input_package[(package_length + 1): package_length + 5]
    package_length += 5

    # print(f'literal_value= {literal_value}')
    return int(literal_value, 2), package_length


def read_operator(input_data: str) -> (List[Packet], int):
    bit_progress = 0
    length_type_id = int(input_data[0], 2)
    bit_progress += 1
    if length_type_id == 0:
        total_length = bit_progress + 15 + int(input_data[bit_progress:bit_progress + 15], 2)
        bit_progress += 15
        sub_packets = []
        while bit_progress < total_length:
            sub_packet, sub_packet_bits = decode_packet(input_data[bit_progress:])
            bit_progress += sub_packet_bits
            sub_packets.append(sub_packet)
        return sub_packets, bit_progress
    else:
        sub_packet_count = int(input_data[bit_progress:bit_progress + 11], 2)
        bit_progress += 11
        sub_packets = []
        for i in range(sub_packet_count):
            sub_packet, sub_packet_count = decode_packet(input_data[bit_progress:])
            bit_progress += sub_packet_count
            sub_packets.append(sub_packet)
        return sub_packets, bit_progress


def decode_packet(input_data: str) -> (Packet, int):
    version = int(input_data[0:3], 2)
    type = int(input_data[3: 6], 2)

    if type == 4:  # literal value
        literal_value, content_length = read_literal(input_data[6:])
        return Literal(version, literal_value), 6 + content_length
    else:  # operator
        sub_packets, content_length = read_operator(input_data[6:])
        return Expression(version, type, sub_packets), 6 + content_length


def hexadecimal_to_binary(hexdecnum):
    binnum = ""
    hexlen = len(hexdecnum)
    i = 0
    while i < hexlen:
        if hexdecnum[i] == '0':
            binnum = binnum + "0000"
        elif hexdecnum[i] == '1':
            binnum = binnum + "0001"
        elif hexdecnum[i] == '2':
            binnum = binnum + "0010"
        elif hexdecnum[i] == '3':
            binnum = binnum + "0011"
        elif hexdecnum[i] == '4':
            binnum = binnum + "0100"
        elif hexdecnum[i] == '5':
            binnum = binnum + "0101"
        elif hexdecnum[i] == '6':
            binnum = binnum + "0110"
        elif hexdecnum[i] == '7':
            binnum = binnum + "0111"
        elif hexdecnum[i] == '8':
            binnum = binnum + "1000"
        elif hexdecnum[i] == '9':
            binnum = binnum + "1001"
        elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
            binnum = binnum + "1010"
        elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
            binnum = binnum + "1011"
        elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
            binnum = binnum + "1100"
        elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
            binnum = binnum + "1101"
        elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
            binnum = binnum + "1110"
        elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
            binnum = binnum + "1111"
        i = i + 1

    return binnum


def get_version_sum(packet: Packet) -> int:
    if isinstance(packet, Literal):
        return packet.version
    elif isinstance(packet, Expression):
        version = packet.version
        for sub_packet in packet.sub_packets:
            version += get_version_sum(sub_packet)
        return version
    else:
        raise ValueError("Unrecognised packet type")


def calculate_expression(packet: Packet) -> int:
    if isinstance(packet, Literal):
        # print(packet.value, end=" ")
        return packet.get_value()
    elif isinstance(packet, Expression):
        if packet.type_id == 0:
            # print('sum', end=" ")
            return sum(calculate_expression(sub_packet) for sub_packet in packet.sub_packets)
        elif packet.type_id == 1:
            # print('product', end=" ")
            return math.prod(calculate_expression(sub_packet) for sub_packet in packet.sub_packets)
        elif packet.type_id == 2:
            # print('minimum', end=" ")
            return min(calculate_expression(sub_packet) for sub_packet in packet.sub_packets)
        elif packet.type_id == 3:
            # print('maximum', end=" ")
            return max(calculate_expression(sub_packet) for sub_packet in packet.sub_packets)
        elif packet.type_id == 5:
            # print('greater than', end=" ")
            sub_packet1 = packet.sub_packets[0]
            sub_packet2 = packet.sub_packets[1]
            if calculate_expression(sub_packet1) > calculate_expression(sub_packet2):
                return 1
            else:
                return 0
        elif packet.type_id == 6:
            # print('less then', end=" ")
            sub_packet1 = packet.sub_packets[0]
            sub_packet2 = packet.sub_packets[1]
            if calculate_expression(sub_packet1) < calculate_expression(sub_packet2):
                return 1
            else:
                return 0
        elif packet.type_id == 7:
            # print('equals', end=" ")
            sub_packet1 = packet.sub_packets[0]
            sub_packet2 = packet.sub_packets[1]
            if calculate_expression(sub_packet1) == calculate_expression(sub_packet2):
                return 1
            else:
                return 0

        else:
            raise ValueError("Unrecognised packet type")


if __name__ == '__main__':
    # This is day 16 (with a 'little' bit of help from Lex van der Stoep)
    filename = "input/input16.txt"
    data = read_input_file(filename)
    data_binary = hexadecimal_to_binary(data)

    print(f'input string= {data}')
    print(f'input binary string= {data_binary}')
    packet, _ = decode_packet(data_binary)
    print(f'part1: sum of versions= {get_version_sum(packet)}')
    print(f'part2: value of expression= {calculate_expression(packet)}')
