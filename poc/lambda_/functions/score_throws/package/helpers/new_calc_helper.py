

def calculate(th, sc = None, frames = None, fr = None):
    
    if sc is None:
        sc = []
    if frames is None:
        frames = []
    if fr is None:
        fr = 1

    '''
    th = [
        {
            'id': 'string',
            'pins': 'string'
        }
    ]
    '''

    def score(x):
        return x['pins']

    def id(x):
        return x['id']

    while True:
        if len(th) == 0:
            break

        t = th.pop(0)
        if score(t) == 'X':
            s = 10
            if score(th[0]) == 'X':
                s += 10
                if score(th[1]) == 'X':
                    s += 10
                else:
                    s += score(th[1])
                    
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        (score(th[1]), id(th[1]))
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                    )
                )
            elif score(th[1]) == '/':
                s += 10
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        (score(th[1]), id(th[1]))
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                    )
                )
            elif score(th[0]) == '-':
                frames.append(
                    (
                        (score(t), id(t)),
                    )
                )
            else:
                s += score(th[0]) + score(th[1])
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        (score(th[1]), id(th[1]))
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                    )
                )
        elif len(th) == 0:
            s = score(t)
            frames.append(
                (
                    (score(t), id(t)),
                    ('-', None)
                )
            )
        elif score(th[0]) == '/':
            s = 10
            if len(th) == 1:
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        ('-', None) 
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0]))
                    )
                )
                score.append(s)
                break
            elif score(th[1]) == 'X':
                s += 10
                frames.append(
                    (
                        (score(t), id(t)), 
                        (score(th[0]), id(th[0])),
                        (score(th[1]), id(th[1]))
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0]))
                    )
                )
            elif score(th[1]) == '-':
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        ('-', None)
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0]))
                    )
                )
            else:
                s += score(th[1])
                frames.append(
                    (
                        (score(t), id(t)),
                        (score(th[0]), id(th[0])),
                        (score(th[1]), id(th[1]))
                    ) if fr == 10 else 
                    (
                        (score(t), id(t)), 
                        (score(th[0]), id(th[0]))
                    )
                )
            th.pop(0)
        elif score(t) == '-':
            break
        elif score(th[0]) == '-':
            s = score(t)
            frames.append(
                (
                    (score(t), id(t)), 
                )
            )
        else:
            s = score(t) + score(th[0])
            p = th.pop(0)
            frames.append(
                (
                    (score(t), id(t)),
                    (score(p), id(p))
                )
            )
    
        sc.append(s)
        fr += 1
        if fr > 10:
            break

    return (frames, sc)


