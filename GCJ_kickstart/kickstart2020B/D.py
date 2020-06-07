import math
T = int(input())
for t in range(1, T+1):
    W, H, L, U, R, D = [int(_) for _ in input().split()]
    res = 0
    def getprob(n, k):
        count = 0
        cur = 1
        count += cur
        for i in range(k):
            cur = cur * (n - i) // (i+1)
            count += cur
        return count / pow(2, n)

    if R < W and U > 1:
        res += getprob(R + U-2, U-2)
    if D < H and L > 1:
        res += getprob(D +L-2, L-2)
    print("Case #{}: {}".format(t, res))