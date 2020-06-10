from functools import lru_cache

T = int(input())
for t in range(1, T+1):
    a, b = input().split()

    @lru_cache(None)
    def getName(i, j, a_error): #aerror be 0 or 1
        if i == len(a) and j == len(b):
            return 0, ''
        if i == len(a):
            res = ''
            left = len(b) - j
            do = left // 2
            res += b[j:j+do]
            j += do * 2
            if j < len(b):
                if a_error == 0:
                    res += b[j]
            return left, res
        if j == len(b):
            res = ''
            left = len(a) - i
            do = left // 2
            res += a[i:i+do]
            i += do * 2
            if i < len(a):
                if a_error == 1:
                    res += a[i]
            return left, res
        if a_error:
            d0, s0 = getName(i+1, j, 0)
            s0 = a[i] + s0
            d1, s1 = getName(i, j+1, 0)
            if d0 < d1:
                res = d0
                ress = s0
            else:
                res = d1
                ress = s1
        else:
            d0, s0 = getName(i+1, j, 1)
            d1, s1 = getName(i, j+1, 1)
            s1 = b[j] + s1
            if d0 < d1:
                res = d0
                ress = s0
            else:
                res = d1
                ress = s1
        res += 1
        if a[i] == b[j]:
            d2, s2 = getName(i+1, j+1, a_error)
            if d2<res:
                res = d2
                ress = a[i] + s2
        elif a_error:
            d2, s2 = getName(i+1, j+1, 0)
            s2 = a[i]+s2
            d2 += 1
            if d2<res:
                res = d2
                ress = s2
        else:
            d2, s2 = getName(i+1, j+1, 1)
            s2 = b[j]+s2
            d2 += 1
            if d2<res:
                res = d2
                ress = s2
        return res, ress

    _, fin = getName(0, 0, 0)
    print("Case #{}: {}".format(t, fin))