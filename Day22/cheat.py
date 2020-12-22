import numpy as np
from copy import deepcopy
with open("input.txt", 'r') as f:
    decks = [list(map(int, sec.splitlines()[1:]))
                     for sec in f.read().split('\n\n')]

def play(d, part):
    if (m := max(d[0])) > max(d[1]) and m > len(d[0]) + len(d[1]):# p0 can't lose
        return 0, d[0]
    seen = set()
    while all(d):
        if (h := str(d)) in seen:
            return 0, d[0]
        seen.add(h)
        c1, c2 = d[0].pop(0), d[1].pop(0)
        w = c2 > c1
        if part == 2 and len(d[0]) >= c1 and len(d[1]) >= c2:
            w, _ = play([d[0][:c1], d[1][:c2]], 2)
        d[w] += [c2, c1] if w else [c1, c2]

    return (0, d[0]) if d[0] else (1, d[1])

score = lambda d: np.array(d).dot(range(len(d), 0, -1))

for r in (1,2):
    print(f'Part {r}:', score(play(deepcopy(decks), r)[1]))