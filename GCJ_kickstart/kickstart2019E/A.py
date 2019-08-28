class DSU:
    def __init__(self, size):
        self.p = list(range(size))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


def solve():
	N, M = [int(_) for _ in input().split()]
	pairs = []
	res = (N-1)*2
	pairs = []
	for _ in range(M):
		pairs.append((int(_) for _ in input().split()))
	dsu = DSU(N+1)
	for a, b in pairs:
		if dsu.find(a) == dsu.find(b):
			pass
		else:
			dsu.union(a, b)
			res -= 1
	return res

T = int(input())
for t in range(1, T+1):
	res = solve()
	print("Case #{}: {}".format(t, res))