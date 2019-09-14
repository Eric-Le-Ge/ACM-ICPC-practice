n, k, m = [int(_) for _ in raw_input().split()]
paths, plans, covered = [[] for _ in range(n)], [[] for _ in range(n)], set()
for i in range(k):
	s, e = [int(_) for _ in raw_input().split()]
	paths[s-1].append(e-1)
for i in range(m):
	s, e = [int(_) for _ in raw_input().split()]
	plans[s-1].append(e-1)
def cover(ind):
	if ind in covered:
		return
	stack = [ind]
	while stack:
		ind = stack.pop()
		covered.add(ind)
		for nind in paths[ind]:
			if nind not in covered:
				stack.append(nind)
res = 0
used = [False]*n
def dfs(ind):
	if ind in covered:
		return
	stack = [ind]
	while stack:
		ind = stack[-1]
		if ind in covered:
			stack.pop()
			continue
		if not used[ind]:
			used[ind] = True
			for nind in paths[ind]:
				stack.append(nind)
		else:
			for e in plans[ind]:
				if e not in covered:
					global res
					res += 1
					cover(ind)
			stack.pop()

for i in range(n):
	dfs(i)

print(res)