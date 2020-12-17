import re

def get_data(fileName = 'test.txt'):
    data = open(fileName,'r').readlines()
    data = [d.strip() for d in data]

    rules =[]
    my_ticket = []
    nearby_tickets = []

    instructions = 'rules'

    for line in data:
        if line == 'your ticket:':
            instructions = 'your ticket'
        elif line == 'nearby tickets:':
            instructions = 'nearby tickets'
        elif instructions == 'rules':
            if line != '':
                rules.append(line)
        elif instructions == 'your ticket':
            if line != '':
                my_ticket = [int(i) for i in line.split(',')]
        elif instructions == 'nearby tickets':
            if line != '':
                nearby_tickets.append(line)
        else:
            raise Exception('Error during parsing of data')
    
    
    rules_numbers = set()
    for line in rules:
        match = re.findall(r"(\d*-\d*)", line)
        m0 = match[0].split('-')
        m1 = match[1].split('-')
        rules_numbers.update([i for i in range(int(m0[0]),int(m0[1])+1)])
        rules_numbers.update([i for i in range(int(m1[0]),int(m1[1])+1)])
    # print(rules, my_ticket, nearby_tickets)
    # print(my_ticket)
    
    # print(rules_numbers)

        
    return rules, my_ticket, nearby_tickets, rules_numbers




def partOne(fileName):
    rules, my_ticket, nearby_tickets, rules_numbers = get_data(fileName)

    invalid_numbers = []
    for ticket in nearby_tickets:
        tick = ticket.split(',')
        for t in tick:
            if int(t) not in rules_numbers:
                invalid_numbers.append(int(t))
    
    print(f"Sum of invalid numbers= {sum(invalid_numbers)}")
    return invalid_numbers

def verify_ticket(ticket, invalid_list):
    for tick in ticket:
        if tick in invalid_list:
            return False
    return True

def validate_column(index, rules, cleaned_nearby_tickets,k):
    low_rule = rules[0]
    hi_rule = rules[1]
    low_rule = [int(i) for i in low_rule]
    hi_rule = [int(i) for i in hi_rule]
    for ticket in cleaned_nearby_tickets:
        if (low_rule[0] <= ticket[index] <= low_rule[1]) or (hi_rule[0] <= ticket[index] <= hi_rule[1]):
            pass
        else:
            return False
    return True

def partTwo(fileName):
    rules, my_ticket, nearby_tickets, rules_numbers = get_data(fileName)
    invalid_numbers = partOne(fileName)
    # print(rules, my_ticket, nearby_tickets, rules_numbers)

    rules_dict = {}
    for rule in rules:
        match = re.findall(r"(.*): (\d*-\d*) or (\d*-\d*)", rule)
        m0 = match[0][1].split('-')
        m1 = match[0][2].split('-')
        rules_dict[match[0][0]] = [m0,m1]
    print(rules_dict)
    # nearby_tickets = [ticket for ticket in nearby_tickets if ticket not in invalid_numbers]
    cleaned_nearby_tickets = []
    for ticket in nearby_tickets:
        ticket = ticket.split(',')
        ticket = [int(tick) for tick in ticket]
        if verify_ticket(ticket, invalid_numbers):
            cleaned_nearby_tickets.append(ticket)
    print(cleaned_nearby_tickets)

    possible_fields = [key for key in rules_dict]
    solutions = {}
    while len(possible_fields) > 0:
        fields_this_run = {}
        for i in range(len(cleaned_nearby_tickets[0])):
            for k, v in rules_dict.items():
                if k not in possible_fields:
                    pass
                elif validate_column(i,v,cleaned_nearby_tickets,k):
                    if i in fields_this_run:
                        fields_this_run[i].append(k)
                    else:
                        fields_this_run[i] = [k]
                    # print(f"{k}: passes column {i}")
                else:       
                    pass         
                    # print(f"Rule {k} failed column {i}")
        for k,v in fields_this_run.items():
            if len(v) == 1:
                print(f"Only possible for Column {k} is {v}")
                solutions[v[0]] =k
                possible_fields.remove(v[0])
        
    print(f"departure time is {my_ticket[solutions['departure time']]}")
    print(f"departure location is {my_ticket[solutions['departure location']]}")
    print(f"departure station is {my_ticket[solutions['departure station']]}")
    print(f"departure platform is {my_ticket[solutions['departure platform']]}")
    print(f"departure track is {my_ticket[solutions['departure track']]}")
    print(f"departure date is {my_ticket[solutions['departure date']]}")
    print("Multiplied together =")
    answer = my_ticket[solutions['departure time']]
    answer *= my_ticket[solutions['departure location']]
    answer *= my_ticket[solutions['departure station']]
    answer *= my_ticket[solutions['departure platform']]
    answer *= my_ticket[solutions['departure track']]
    answer *= my_ticket[solutions['departure date']]
    print(answer)





if __name__=='__main__':
    # partOne('C:\\Users\\tyrda\\OneDrive\\Programming\\AdventOfCode\\2020\\Day16\\input.txt')

    partTwo('C:\\Users\\tyrda\\OneDrive\\Programming\\AdventOfCode\\2020\\Day16\\input.txt')
