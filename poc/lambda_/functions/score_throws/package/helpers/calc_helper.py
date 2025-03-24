

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
            if len(th) == 1:
                frames.append((t, th[0], '-') if fr == 10 else (t, th[0]))
                score.append(s)
                break
            elif th[1] == 'X':
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

