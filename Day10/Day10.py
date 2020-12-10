from datetime import datetime
data = []
with open('/home/pi/Programming/AdventOfCode/2020/Day10/input.txt','r') as f:
    data = [int(i.strip()) for i in f.readlines()]
    data.append(0)
    data.sort()


volt_dict = {1:0,3:1} # 3:1 exists because our phone has a default +3 setting
previous_voltage = 0
for adapter in data:
    volt_difference = adapter - previous_voltage
    previous_voltage = adapter

    if volt_difference in volt_dict:
        volt_dict[volt_difference] += 1
    else:
        volt_dict[volt_difference] = 1
# data = [1,4,5,6]
data.append(data[-1]+3)
print(data)
print(volt_dict)

adapter_dict = {}
def search_adapters(index):
    if index in adapter_dict:
        # we've already discovered this
        return adapter_dict[index]
    elif index == len(data) - 1:
        # Success!, We've hit the last node
        return 1
    elif index >= len(data):
        # We've gone too far
        return 0
    else:
        # We take the next three indexes on the list
        a,b,c = index +1, index +2, index +3
        current_targets = [data[index]+1, data[index]+2, data[index]+3]
        val_a, val_b, val_c = 0,0,0
        if (data[index+1])  in current_targets:
            val_a = search_adapters(a)
        if (index+2 < len(data)) and (data[index + 2])  in current_targets:
            val_b = search_adapters(b)
        if (index+3 < len(data)) and (data[index + 3])  in current_targets:
            val_c = search_adapters(c)

        current_values = val_a + val_b + val_c
        #adapter_dict[index] = current_values
        return current_values

start = datetime.now()
print(search_adapters(0))
print(dict(sorted(adapter_dict.items())))
time = datetime.now() - start
print(time)
    