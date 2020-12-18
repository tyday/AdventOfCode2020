
def partOne(input, total=2020):
    turn = 1
    last_say = ''
    turn_dict = {}

    for i in range(len(input)-1):
        turn_dict[input[i]] = turn
        turn += 1
    last_say = input[-1]
    
    while turn < total:
        say = ''
        if last_say in turn_dict:
            # todo
            say = turn  - turn_dict[last_say]
            turn_dict[last_say] = turn
        else:
            say = 0
            turn_dict[last_say] = turn
        turn +=1
        last_say = say
        # print(f"Turn {turn}: {say}")
    return say



if __name__=='__main__':
    print(partOne([2,15,0,9,1,20],30000000))