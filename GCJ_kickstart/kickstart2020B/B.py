import math
T = int(input())
for t in range(1, T+1):
    n, d = [int(_) for _ in input().split()]
    data = [int(_) for _ in input().split()]
    lo, hi = 1, d+1

    def can(x):
        for item in data:
            x = item * math.ceil(x/item)
            if x > d:
                return False
        return True

    while hi-lo>1:
        mid = (lo+hi)//2
        if can(mid):
            lo = mid
        else:
            hi = mid

    print("Case #{}: {}".format(t, lo))
