from collections import Counter
import sys
for line in sys.stdin:
    s = line.strip('\n')
    def fac(n):
        res = 1
        while n>1:
            res *= n
            n -= 1
        return res
    c = Counter(s)
    total = fac(len(s))
    for v in c.values():
        total //= fac(v)
    print total

