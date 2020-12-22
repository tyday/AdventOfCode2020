import copy, datetime

def get_data(fileName):
    with open(fileName, 'r') as f:
        decks = [[],[]]
        data = f.read().split('\n')
        player = 0
        for line in data:
            if line == '':
                player += 1
            elif line.startswith('Player'):
                pass
            else:
                decks[player].append(int(line))
        return decks

def playRound(decks):
    player1 = decks[0]
    player2 = decks[1]
    p1_card = player1.pop(0)
    p2_card = player2.pop(0)

    winner = 0

    if p1_card > p2_card:
        # player one wins thing
        player1 += [p1_card,p2_card]
        winner = 1
    elif p2_card > p1_card:
        # player two wins thing
        player2 += [p2_card, p1_card]
        winner = 2
    else:
        # we have a tie.
        # the rules aren't clear on this
        print('There was a tie')
    return winner, [player1, player2]

def playGame(decks):
    turns = 0
    winner = -1
    while len(decks[0]) > 0 and len(decks[1])>0:
        turns += 1
        winner, decks = playRound(decks)
    if len(decks[0]) > len(decks[1]):
        winner = 0
        # print(f'Player 1 won! on turn {turns}')
        # print(decks[0])
        # return 0
    else:
        winner = 1
        # print(f'Player 2 won! on turn {turns}')
        # print(decks[1])
        # return 1
    print(f'Player {winner + 1} won! on turn {turns}')
    print(decks[winner])
    score = 0
    index = 0
    for card in decks[winner]:
        score += card * (len(decks[winner]) - index )
        index += 1
    print(score)
    return score

def convert_decks_to_string(decks):
    player = 1
    returnString = ''
    for deck in decks:
        returnString += f'p{player} '
        returnString += " ".join([str(i) for i in deck])
        player += 1
    return returnString

def playRecursiveGame(decks, game_dict):
    # game_name = convert_decks_to_string(decks)
    winner = 0
    gm_dict = {}
    while len(decks[0]) != 0 and len(decks[1]) !=0:
        game_name = convert_decks_to_string(decks)
        # if game_name in game_dict:
        if game_name in gm_dict:
            return 1, decks
        elif len(decks[0]) - 1 >= decks[0][0] and len(decks[1]) - 1 >= decks[1][0]:
            # Both players have >= cards in deck as their top card's value
            # game_dict[convert_decks_to_string(decks)] = 1
            p1_card = decks[0].pop(0)
            p2_card = decks[1].pop(0)

            player1 = decks[0][:p1_card]
            player2 = decks[1][:p2_card]
            round_winner, rec_decks = playRecursiveGame([player1,player2], game_dict)
            gm_dict[game_name] = round_winner
            if round_winner == 1:
                decks[0] += [p1_card,p2_card]
            else:
                decks[1] += [p2_card,p1_card]
            

        else:
            # play a normal game
            # game_dict[convert_decks_to_string(decks)] = 1
            round_winner, decks = playRound(decks)
            gm_dict[game_name] = round_winner
    
    if len(decks[0]) == 0:
        winner = 2
    else:
        winner = 1
    return winner, decks
        




def partOne(fileName):
    data = get_data(fileName)
    # print(data)
    playGame(data)

def partTwo(fileName):
    game_dict = {}
    decks = get_data(fileName)
    # while len(decks[0]) != 0 and len(decks[1]) !=0:
    winner, decks = playRecursiveGame(decks, game_dict)
    
    score = 0
    index = 0
    for card in decks[winner-1]:
        score += card * (len(decks[winner-1]) - index )
        index += 1
    print(decks)
    print(f'Player {winner} won the game with final hand: {decks[winner-1]}')
    print(f'Score: {score}')


if __name__=='__main__':
    # partOne('/home/pi/Programming/AdventOfCode/2020/Day22/input.txt')
    # print(convert_decks_to_string([[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]))

    start = datetime.datetime.now()
    partTwo('/home/pi/Programming/AdventOfCode/2020/Day22/input.txt')
    print(f'Finished in {datetime.datetime.now() -start}')