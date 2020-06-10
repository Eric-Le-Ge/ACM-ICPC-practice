T = int(input())
for t in range(1, T+1):
    K, N = [int(_) for _ in input().split()]
    l = [int(_) for _ in input().split()]
    input()
    sav = l
    res_ = 2 * N
    for _ in range(N):
        a = l[0]
        for j in range(len(l)):
            l[j] -= a
        l.append(K)
        res = 1
        start, end = l[0], l[1]
        ds = [l[i+1] - l[i] for i in range(len(l)-1)]
        done = False
        i = 1
        while i < len(l) - 1:
            res += 1
            range_start = l[i]
            range_end = l[i+1]
            start_place = 2 * range_start - end
            end_place = 2 * range_start - start
            end_place = min(end_place, range_end)

            #if not end_place > start_place: # reset
            #    end = range_start
            if not end_place > start_place: # reset
                if not done:
                    done = True
                    # bp for segment A
                    for j in range(i-1, 0, -1):
                        prevstart, prevend = l[j-1], l[j]
                        start, end = prevend * 2 - end, prevend * 2 - start
                        start, end = max(prevstart, start), min(prevend, end)
                    backstart, backend = start, end
                start, end = l[i-1], l[i]
            else:
                start, end = start_place, end_place
                i += 1

        # last case wrap around
        start_place = K - end
        end_place = K - start
        end_place = min(end_place, l[1])

        if res > len(l) - 1: # independent
            if (not end_place > start_place) or (done and (start_place >= backend or end_place <= backstart)):
                res += 1
        else: # dependent
            if not end_place > start_place:
                res += 1
            elif len(l) % 2 == 1: # even
                if not sum([ds[i] * ((-1) ** i) for i in range(len(ds))]) == 0:
                    res += 1
            else: # odd
                z = sum([ds[i] * ((-1) ** i) for i in range(len(ds))]) / 2
                # run propagate
                for i in range(len(ds)):
                    if z >= ds[i]:
                        res += 1
                        break
                    z = ds[i] - z
        res_ = min(res_, res)
        l.pop()
        l.append(l.pop(0) + K)

    print("Case #{}: {}".format(t, res_))