def get_row(row_code):
    row_code = row_code.replace("F", "0")
    row_code = row_code.replace("B", "1")
    return int(row_code,2)

def get_column(column_code):
    column_code = column_code.replace("L", "0")
    column_code = column_code.replace("R", "1")
    return int(column_code, 2)
row = get_row('FBFBBFF')
column = get_column('RLR')

def get_seat_code(seat_info):
    row = get_row(seat_info[:7])
    column = get_column(seat_info[7:])
    return row * 8 + column
# print(get_seat_code('BFFFBBFRRR'))
# print(get_seat_code('FFFBBBFRRR'))
# print(get_seat_code('BBFFBBFRLL'))
# print(get_seat_code('BBBBBBBRRR'))

max_value = 0
with open('Day05.txt') as f:
    for line in f:
        value = get_seat_code(line.strip())
        if value>max_value:
            max_value = value
print(max_value)

open_seats = [a for a in range(856)]
errors = []
with open('Day05.txt') as f:
    for line in f:
        value = get_seat_code(line.strip())
        try:
            open_seats.remove(value)
        except:
            errors.append(value)
print(open_seats)
print(errors)