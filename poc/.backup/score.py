import copy
import itertools

throws = [9, '/', 'X', 8, 1, 'X', 'X', 7, 0, 9, '/', 'X', 0, '/', 'X', 'X', 9]
throws.pop()
throws.pop()
throws.pop()
throws.append(7)

best_possible = [('X',) for _ in range(9)]
best_possible.append(('X', 'X', 'X'))

#thr = copy.copy(throws)

def calculate(th, score = None, frames = None, fr = None):
    
    if score is None:
        score = []
    if frames is None:
        frames = []
    if fr is None:
        fr = 1

    while True:
        t = th.pop(0)
        if t == 'X':
            s = 10
            if th[0] == 'X':
                s += 10
                if th[1] == 'X':
                    s += 10
                    frames.append(('X', 'X', 'X') if fr == 10 else ('X',))
                else:
                    s += th[1]
                    frames.append(('X', 'X', th[1]) if fr == 10 else ('X',))
            elif th[1] == '/':
                s += 10
                frames.append(('X', th[0], '/') if fr == 10 else ('X',))
            elif th[0] == '-':
                frames.append(('X',))
            else:
                s += th[0] + th[1]
                frames.append(('X', th[0], th[1]) if fr == 10 else ('X',))
        elif len(th) == 0:
            s = t
            frames.append((t, '-'))
        elif th[0] == '/':
            s = 10
            if th[1] == 'X':
                s += 10
                frames.append((t, th[0], 'X') if fr == 10 else (t, th[0]))
            elif th[1] == '-':
                frames.append((t, th[0], '-') if fr == 10 else (t, th[0]))
            else:
                s += th[1]
                frames.append((t, th[0], th[1]) if fr == 10 else (t, th[0]))
            th.pop(0)
        elif t == '-':
            break
        elif th[0] == '-':
            s = t
            frames.append((t, ))
        else:
            s = t + th[0]
            frames.append((t, th.pop(0)))
    
        score.append(s)
        fr += 1
        if fr > 10:
            break

    return (frames, score)

(frames, score) = calculate(copy.copy(throws))

print(frames)
print(list(itertools.accumulate(score)))

print('#########')

_last_fr_l = len(frames)
_last_fr = frames[-1]


if _last_fr_l == 10:
    a = None
    b = None
    c = None
    if len(_last_fr) == 1:
        a = _last_fr[0]
    if len(_last_fr) == 2:
        a, b = _last_fr
    if len(_last_fr) == 3:
        a, b, c = _last_fr

    if '-' not in [a, b, c]:                            # frame is completed
        _last_fr = last_fr
    elif a == '-':                                      # frame not started
        _last_fr = ('X', 'X', 'X')
    elif a in range(10) and b == '-':                   # first ball, not a strike
        _last_fr = (a, '/', 'X')
    elif a in range(10) and b in range(10):             # first ball, no spare
        _last_fr = (a, b)
    elif a in range(10) and b == '/' and c == '-':      # first ball, spare, no third
        _last_fr = (a, '/', 'X')
    elif a == 'X' and b == '-':                         # first ball strike
        _last_fr = (a, 'X', 'X')
    elif a == 'X' and b in range(10):                   # first ball strike, second not a strike
        _last_fr = (a, b, '/')
    elif a == 'X' and b == 'X':                         # first ball strike, second ball strike
        _last_fr = (a, b, 'X')
else:
    a = None
    b = None
    if len(_last_fr) == 1:
        a = _last_fr[0]
    if len(_last_fr) == 2:
        (a, b) = _last_fr

    if a == 'X':                                        # first ball strike
        _last_fr = _last_fr
    elif a in range(10) and b is None:                  # first ball, not a strike
        _last_fr = (a, '/')
    elif a in range(10) and b in range(10):             # first ball not a strike, no spare
        _last_fr = (a, b)
    else:
        print(f'a is {a} and b is {b}')

for i, each in enumerate(frames[:-1]):
    #print(f'{i} :: {each}')
    best_possible[i] = each

best_possible[_last_fr_l - 1] = _last_fr

flattened_best = [t for w in best_possible for t in w]

print(f'flattened: {flattened_best}')

(bfr, sc) = calculate(copy.copy(flattened_best))
print(bfr)
print(list(itertools.accumulate(sc)))
#print(f'best possible: {list(itertools.accumulate(sc))[-1]}')


