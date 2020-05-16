T = int(input())
for t in range(1, T+1):
    x, y = [int(_) for _ in input().split()]
    done = False
    res = []
    for start in range(35, -1, -1):
        step = 1 << start
        ret = []
        curx, cury = x, y
        good = False
        while step:
            if abs(curx) >= abs(cury):
                if curx > 0:
                    curx -= step
                    ret.append('E')
                else:
                    curx += step
                    ret.append('W')
            else:
                if cury > 0:
                    cury -= step
                    ret.append('N')
                else:
                    cury += step
                    ret.append('S')
            step = step // 2
        if curx == 0 and cury == 0:
            good = True
        if good:
            res = ret
            done = True


    if not done:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue
    print("Case #{}: {}".format(t, "".join(res[::-1])))