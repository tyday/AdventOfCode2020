timestamp = 1014511
businfo = '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'

def product(numbs):
    total = 1
    for i in numbs:
        total *= i
    return total

businfo = businfo.split(',')
print(businfo)
earliest_time = None
# for bus in businfo:
#     if bus != 'x':
#         iterator = 0
#         while iterator < timestamp:
#             iterator+= int(bus)
#         if not earliest_time:
#             earliest_time = (bus, iterator)
#         else:
#             if iterator < earliest_time[1]:
#                 earliest_time = (bus, iterator)
# print(earliest_time)
# print("wait =", earliest_time[1]-timestamp)
# print("Code =", (earliest_time[1]-timestamp)*int(earliest_time[0]))

# buses = [int(i) for i in businfo if i !='x']
buses = {x:businfo.index(x) for x in businfo}
# buses = [2,3,4,7]
print(buses)
i = 1
def all_buses(buses, i):
    test = i * max(buses)
    for bus in buses:
        if ((test) % bus) != 0:
            return False
    return True
found = False
# while i * max(buses) < 100: #10168781:
# while not found:
#     i += 1
#     if all_buses(buses, i):
#         found = True
#         print(f"i: {i}, i * {min(buses)} : {i*min(buses)}")
def chinese_remainder(n, a):
    p = product(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p

inputs = [(int(x), int(x) - p) for p, x in enumerate(businfo) if x != "x"]
print([(x,p) for p,x in enumerate(businfo) if x != "x"])
print(inputs)
print(chinese_remainder([x[0] for x in inputs], [x[1] for x in inputs]))