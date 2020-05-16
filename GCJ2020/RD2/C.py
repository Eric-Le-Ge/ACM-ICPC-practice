from math import gcd
T = int(input())

for t in range(1, T+1):
    N = int(input())

    points = []
    for i in range(N):
        points.append([int(_) for _ in input().split()])
    res = 1
    pairs = {}
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx, dy = x2-x1, y2-y1
            if dx == 0:
                dy = 1
            elif dy == 0:
                dx = 1
            else:
                div = gcd(abs(dx), abs(dy))
                dx //= div
                dy //= div
                if dx < 0:
                    dx, dy = -dx, -dy
            if (dx, dy) not in pairs:
                pairs[(dx, dy)] = set()
            pairs[(dx, dy)].add(i)
            pairs[(dx, dy)].add(j)
    for k, v in pairs.items():
        count = len(v)
        if count % 2 == 1:
            res = max(count+1, res)
        else:
            res = max(count+2, res)
    print("Case #{}: {}".format(t, min(res, N)))