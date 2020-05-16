from fractions import Fraction
from collections import defaultdict
from math import gcd
T = int(input())
for t in range(1, T+1):
    N, D = [int(_) for _ in input().split()]
    data = [int(_) for _ in input().split()]
    lo, hi = 1, (max(data)+1)*10000

    def can(num):
        s = 0
        for d in data:
            s += d*10000//num
            if s >= D:
                return True
        return False
    for _ in range(40):
        mid = (hi+lo)//2
        if can(mid):
            lo = mid
        else:
            hi = mid
    hi = hi / 10000
    m = {} #full use, total slices
    K = 1
    for c in range(1, D+1):
        for d in data:
            f = (d//gcd(d, c), c//gcd(d, c))
            if f not in m:
                m[f] = (1, c)
                continue
            count = c
            if m[f][1] + count > D or f[0] >= hi*f[1]:
                continue
            m[f] = (m[f][0]+1, m[f][1]+c)
            K = max(K, m[f][0])

    print("Case #{}: {}".format(t, D-K))