T, a, b = [int(_) for _ in input().split()]
candidates = []
for x in [0, 250000000, 500000000, 750000000]:
    for y in [0, 250000000, 500000000, 750000000]:
        candidates.append((x, y))
        candidates.append((-x, y))
        candidates.append((x, -y))
        candidates.append((-x, -y))

for t in range(1, T+1):
    centx, centy = -1, -1
    done = False
    for x, y in candidates:
        print(str(x) + " " + str(y), flush=True)
        ver = input()
        if ver == "CENTER":
            done = True
            break
        elif ver == "HIT":
            centx, centy = x, y
            break
    if done:
        continue
    if centy==-1 and centx==-1:
        pass
    #binsearch
    lo, hi = centx, 1000000001
    while hi-lo>1:
        mid = (hi+lo)//2
        print(str(mid) + " " + str(y), flush=True)
        ver = input()
        if ver == "CENTER":
            done = True
            break
        elif ver == "HIT":
            lo = mid
        else:
            hi = mid
    topx = lo
    if done == True:
        continue

    #binsearch
    lo, hi = centx, -1000000001
    while lo-hi>1:
        mid = (hi+lo+1)//2
        print(str(mid) + " " + str(y), flush=True)
        ver = input()
        if ver == "CENTER":
            done = True
            break
        elif ver == "HIT":
            lo = mid
        else:
            hi = mid
    botx = lo
    if done == True:
        continue

    #binsearch
    lo, hi = centy, 1000000001
    while hi-lo>1:
        mid = (hi+lo)//2
        print(str(centx) + " " + str(mid), flush=True)
        ver = input()
        if ver == "CENTER":
            done = True
            break
        elif ver == "HIT":
            lo = mid
        else:
            hi = mid
    topy = lo
    if done == True:
        continue

    #binsearch
    lo, hi = centy, -1000000001
    while lo-hi>1:
        mid = (hi+lo+1)//2
        print(str(centx) + " " + str(mid), flush=True)
        ver = input()
        if ver == "CENTER":
            done = True
            break
        elif ver == "HIT":
            lo = mid
        else:
            hi = mid
    boty = lo
    if done == True:
        continue

    resx, resy = (topx+botx)//2, (topy+boty)//2

    for dx in range(-5, 5):
        for dy in range(-5, 5):
            px, py = resx+dx, resy+dy
            print(str(px) + " " + str(py), flush=True)
            ver = input()
            if ver == "CENTER":
                done = True
                break
        if done == True:
            break
    if not done:
         1/0
