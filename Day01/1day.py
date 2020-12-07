data = []
answer = None
with open('E:\LocalProgramming\\advent2020\\1day.txt', 'r') as f:
    for line in f.readlines():
        data.append(int(line.strip('\n')))


## Part One
# for datum in data:
#     b = 2020 - datum
#     if b in data:
#         answer = (datum, b)
#         break
# print(answer)

## Part Two
for a in data:
    bc = 2020 - a
    for b in data:
        c = bc - b
        if c in data:
            answer = (a,b,c)
            break

print(answer)
print(answer[0]*answer[1]*answer[2])