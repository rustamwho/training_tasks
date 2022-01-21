from dataclasses import dataclass
from math import prod

OPERATIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda subs: subs[0] > subs[1],
    6: lambda subs: subs[0] < subs[1],
    7: lambda subs: subs[0] == subs[1],
}


@dataclass
class Packet:
    """ For storage packets. """
    version: int
    type_id: int
    body: str


def _create_packet(packet: str):
    """ Return Packet object. """
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    body = packet[6:]
    return Packet(version=version, type_id=type_id, body=body)


def decode_packet(packet: str) -> tuple[int, int, str]:
    """
    Return <sum_all_subpackets_versions>, <result_after_operations>, <packet>.
    Recursion function.
    """
    packet = _create_packet(packet)
    type_id = packet.type_id
    sum_of_versions = packet.version

    # For literal value packet. Return single
    if packet.type_id == 4:
        todo = packet.body
        value = ''
        while todo.startswith('1'):
            value += str(todo[1:5])
            todo = todo[5:]
        value += str(todo[1:5])
        value = int(value, 2)
        return sum_of_versions, value, todo[5:]

    sub_packets_values = []

    if packet.body[0] == '0':
        # The next 15 bits are a number that represents the total length in
        # bits of the sub-packets contained by this packet
        sub_packets_length = int(packet.body[1:16], 2)
        todo = packet.body[16:16 + sub_packets_length]  # Subpackets
        packet = packet.body[16 + sub_packets_length:]  # Rest of the packet
        # Decode all subpackets
        while todo:
            sub_version, value, todo = decode_packet(todo)
            sum_of_versions += sub_version
            sub_packets_values.append(value)
    else:
        # The next 11 bits are a number that represents the number of
        # sub-packets immediately contained by this packet
        sub_packets_count = int(packet.body[1:12], 2)
        packet = packet.body[12:]
        # Decode all subpackets
        for _ in range(sub_packets_count):
            sub_version, value, packet = decode_packet(packet)
            sum_of_versions += sub_version
            sub_packets_values.append(value)

    return sum_of_versions, OPERATIONS[type_id](sub_packets_values), packet


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_packet = file.read().strip()
    input_packet = ''.join(f'{int(x, 16):04b}' for x in input_packet)

    part1, part2, _ = decode_packet(input_packet)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
