T = int(input())
for t in range(1, T+1):
    n = int(input())
    activities_ = []
    for i in range(n):
        activities_.append([int(_) for _ in input().split()])
    activities = [(i, activities_[i][0], activities_[i][1]) for i in range(n)]
    activities.sort(key=lambda x: x[1])
    aok = True
    aend = 0
    bok = True
    bend = 0
    res = ['']*n
    bad = False
    for i, start, end in activities:
        if start >= aend:
            aok = True
        if start >= bend:
            bok = True
        if aok:
            aend = end
            res[i] = 'J'
            aok = False
        elif bok:
            bend = end
            res[i] = 'C'
            bok = False
        else:
            bad = True
            break
    if bad:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        print("Case #{}: {}".format(t, "".join(res)))

