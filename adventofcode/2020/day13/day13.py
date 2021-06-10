import math


def select_bus(time, buses_list):
    """Поиск автобуса с минимальным ожиданием"""
    buses = {}
    for bus in buses_list:
        wait_time = math.ceil(time / bus) * bus - time
        buses[bus] = wait_time
    bus = min(buses, key=buses.get)
    return bus, buses[bus]


def search_timestamp(buses_dict):
    """
    Поиск timestamp, чтобы каждый автобус начинал свое движение со своим
    отклонением от него
    Номера автобусов - взаимно простые числа, поэтому шаг умножается на
    очередной номер
    """
    timestamp = 1
    step = 1
    for bus, time in buses_dict.items():
        while (timestamp + time) % bus != 0:
            timestamp += step
        step *= bus
    return timestamp


def search_bus():
    """Первая часть"""
    with open('input.txt', 'r') as file:
        time, input_buses = file.read().splitlines()
    buses = [int(bus) for bus in input_buses.split(',') if bus != 'x']
    bus, wait_time = select_bus(int(time), buses)
    result = bus * wait_time
    print(f"Time: {time}\nBus: {bus}\nWait time: {wait_time}\nPart 1: {result}")
    return input_buses


def search_bus_part2(buses_list):
    """Вторая часть"""
    buses = {}
    i = 0
    for bus in buses_list.split(','):
        if bus != 'x':
            buses[int(bus)] = i
        i += 1
    timestamp = search_timestamp(buses)
    print(f"Part 2: {timestamp}")


input_buses = search_bus()
search_bus_part2(input_buses)
