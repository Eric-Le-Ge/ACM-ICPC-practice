T = int(input())

for t_ in range(1, T+1):
    n = int(input())
    data = []
    middles = [[] for _ in range(n)]
    heads = [[] for _ in range(n)]
    tails = [[] for _ in range(n)]
    res = ''
    for _ in range(n):
        data.append(input())

    for i, s in enumerate(data):
        if '*' not in s:
            res = s
        parts = s.split('*')
        if s[0] != '*':
            heads[i].append(parts[0])
        if s[-1] != '*':
            tails[i].append(parts[-1])
        if s[0] != '*':
            parts.pop(0)
        if s[-1] != '*':
            parts.pop(-1)
        middles[i].extend(parts)

    good = True
    if res:
        for i in range(n):
            h = '' if not heads[i] else heads[i][0]
            if len(h) > len(res):
                good = False
                break
            if h != res[:len(h)]:
                good = False
                break
            t = '' if not tails[i] else tails[i][0]
            if len(t) > len(res):
                good = False
                break
            if t != res[len(res)-len(t):]:
                good = False
                break
            if not middles[i]:
                continue
            tmp = res[len(h):len(res)-len(t)]
            for m in middles[i]:
                if m not in tmp:
                    good = False
                    break
                ind = tmp.index(m)
                tmp = tmp[ind + len(m):]
        if not good:
            break
    if not good:
        print("Case #{}: *".format(t_))
        continue
    elif res:
        print("Case #{}: *".format(t_))

    lhead = ''
    ltail = ''

    for i in range(n):
        if not heads[i]:
            continue
        h = heads[i][0]
        if len(h) > len(lhead):
            if lhead != h[:len(lhead)]:
                good = False
                continue
            lhead = h
        else:
            if h != lhead[:len(h)]:
                good = False
                continue

    for i in range(n):
        if not tails[i]:
            continue
        t = tails[i][0]
        if len(t) > len(ltail):
            if ltail != t[len(t)-len(ltail):]:
                good = False
                continue
            ltail = t
        else:
            if t != ltail[len(ltail)-len(t):]:
                good = False
                continue

    if not good:
        print("Case #{}: *".format(t_))
        continue
    res = []
    for m in middles:
        res.extend(m)
    res = ''.join(res)
    res = lhead + res + ltail
    print("Case #{}: {}".format(t_, res))