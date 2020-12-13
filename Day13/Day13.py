timestamp = 1014511
businfo = '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,433,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
businfo = businfo.split(',')
print(businfo)
earliest_time = None
for bus in businfo:
    if bus != 'x':
        iterator = 0
        while iterator < timestamp:
            iterator+= int(bus)
        if not earliest_time:
            earliest_time = (bus, iterator)
        else:
            if iterator < earliest_time[1]:
                earliest_time = (bus, iterator)
print(earliest_time)
print("wait =", earliest_time[1]-timestamp)
print("Code =", (earliest_time[1]-timestamp)*int(earliest_time[0]))