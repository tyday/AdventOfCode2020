import sys
from collections import deque

game_amt = 1

def play_game(p1, p2, game_num):
    # print(f'\n=== Game {game_num} ===')
    seen = set()
    round_num = 1
    # continue playing a round until someone is out of cards OR
    # until a previous state is seen
    while p1 and p2:
        if play_round(p1, p2, seen, game_num, round_num) != None:
            # print(f'State seen previously. The winner of game {game_num} is player 1!\n')
            return 'p1'
        round_num += 1
    # print(f'The winner of game {game_num} is player {1 if p1 else 2}!\n')
    return 'p1' if p1 else 'p2'

def play_round(p1, p2, seen, game_num, round_num):
    # print(f'\n-- Round {round_num} (Game {game_num}) --')
    # print(f'Player 1\'s deck: {", ".join(map(str, p1))}')
    # print(f'Player 2\'s deck: {", ".join(map(str, p2))}')
    
    # if we have seen this exact configuration before in this game
    # player 1 wins instantly
    config = str(p1) + str(p2)
    if config in seen:
        return 'p1'
    seen.add(config)

    card1 = p1.popleft()
    card2 = p2.popleft()
    # print(f'Player 1 plays: {card1}')
    # print(f'Player 2 plays: {card2}')
    
    # play a subgame if there are enough cards
    if card1 <= len(p1) and card2 <= len(p2):
        newp1 = deque(list(p1)[:card1])
        newp2 = deque(list(p2)[:card2])

        # print('Playing a sub-game to determine the winner...')
        global game_amt
        game_amt += 1
        winner = play_game(newp1, newp2, game_amt)
        # print(f'...anyway, back to game {game_num}.')

        # winner of the subgame determines winner of this round
        if winner == 'p1':
            # print(f'Player 1 wins round {round_num} of game {game_num}!')
            p1.append(card1)
            p1.append(card2)
        else:
            # print(f'Player 2 wins round {round_num} of game {game_num}!')
            p2.append(card2)
            p2.append(card1)
    
    # without enough cards, the round plays normally
    else:
        if card1 > card2:
            # print(f'Player 1 wins round {round_num} of game {game_num}!')
            p1.append(card1)
            p1.append(card2)
        else:
            # print(f'Player 2 wins round {round_num} of game {game_num}!')
            p2.append(card2)
            p2.append(card1)

with open(sys.argv[1]) as f:
    p1, p2 = f.read().split('\n\n')

p1 = deque(map(int, p1.split('\n')[1:]))
p2 = deque(map(int, p2.split('\n')[1:]))

score = 0
winner = play_game(p1, p2, game_amt)

# print('\n== Post-game results ==')
# print(f'Player 1\'s deck: {", ".join(map(str, p1))}')
# print(f'Player 2\'s deck: {", ".join(map(str, p2))}')

if winner == 'p1':
    while p1:
        score += len(p1) * p1.popleft()
else:
    while p2:
        score += len(p2) * p2.popleft()

print(f'Winner\'s score: {score}')