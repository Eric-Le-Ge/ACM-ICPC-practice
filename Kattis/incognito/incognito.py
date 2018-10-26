import sys
n = int(sys.stdin.readline())
for i in range(n):
    categories = {}
    j = int(sys.stdin.readline())
    for k in range(j):
        c = sys.stdin.readline().split(" ")[1]
        if c in categories:
            categories[c] += 1
        else:
            categories[c] = 2
    res = 1
    for k,v in categories.items():
        res*=v
    print res-1
