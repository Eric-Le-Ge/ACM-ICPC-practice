# t = int(input())
# for i in range(1, t + 1):
#   n, m = [int(s) for s in input().split(" ")]
#   print("Case #{}: {} {}".format(i, n + m, n * m))

t = int(input())
for i in range(1, t + 1):
    strs = set()
    n, p = [int(s) for s in input().split(" ")]
    for s in range(p):
        strs.add(input())
    strs1 = strs.copy()

    for s in strs1:
        for j in range(len(s)):
            if s[0:j] in strs1:
                strs.remove(s)
                break
    
    res = 2**n
    for s in strs:
        res -= 2**(n-len(s))
    print("Case #{}: {}".format(i, res))
