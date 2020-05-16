T = int(input())
for t in range(1, T+1):
    l, r = [int(_) for _ in input().split()]
    #first bin search
    def can1(num):
        if max(l, r) - ((1 + num) * num) // 2 < min(r, l):
            return False
        return True
    #l is eq or more
    lo, hi = 0, 10000000000000000
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if can1(mid):
            lo = mid
        else:
            hi = mid
    res = lo
    if l >= r:
        l -= ((1 + lo) * lo) // 2
    else:
        r -= ((1 + lo) * lo) // 2

    #second bin search

    def can2(num):
        start = res + 2
        end = res + (num-1) * 4 + 4
        if min(r, l) - ((start + end) * (num * 2)) // 2 >= 0:
            return True
        return False
    lo, hi = 0, 10000000000000000
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if can2(mid):
            lo = mid
        else:
            hi = mid

    startr, endr = res + 2, res + (lo-1) * 4 + 4
    startl, endl = res + 1, res + (lo-1) * 4 + 3
    if l >= r:
        r -= (startr + endr) * (lo * 2) // 2
        l -= (startl + endl) * (lo * 2) // 2
    else:
        l -= (startr + endr) * (lo * 2) // 2
        r -= (startl + endl) * (lo * 2) // 2

    res += lo * 4

    if l >= r:

        if l >= res + 1:
            res += 1
            l -= res
            if r >= res + 1:
                res += 1
                r -= res
                if l >= res + 1:
                    res += 1
                    l -= res

    else:
        if r >= res + 1:
            res += 1
            r -= res
            if l >= res + 1:
                res += 1
                l -= res
                if r >= res + 1:
                    res += 1
                    r -= res

    print("Case #{}: {} {} {}".format(t, res, l, r))
