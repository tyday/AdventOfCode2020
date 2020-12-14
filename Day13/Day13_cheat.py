# from math import prod D   

with open("13.in") as f:
    data = f.read().splitlines()

def prod(numbs):
    total = 1
    for i in numbs:
        total *= i
    return total

earliest_start = int(data[0])
buses = [int(x) for x in data[1].split(",") if x != "x"]

departing = [(-1 * earliest_start) % x for x in buses]

earliest_bus = sorted([[x, y] for x, y in zip(buses, departing)], key=lambda b: b[1])[0]

print(prod(earliest_bus))


def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


inputs = [(int(x), int(x) - p) for p, x in enumerate(data[1].split(",")) if x != "x"]

print(chinese_remainder([x[0] for x in inputs], [x[1] for x in inputs]))