T = int(raw_input())


def solve():
	K, N = [int(_) for _ in raw_input().split()]
	spots = [int(_) for _ in raw_input().split()]
	costs = [int(_) for _ in raw_input().split()]
	res = 0
	for i in range(N):
		cost= costs[i]
		tmp = []
		for j in range(N):
			if j != i:
				tmp.append(costs[j]+abs(spots[i]-spots[j]))
		best = sum(sorted(tmp)[:K])+cost
		if res == 0:
			res = best
		else:
			res = min(res, best)
	return res


for t in range(T):
	res = solve()
	print "Case #{}: {}".format(t+1, res)