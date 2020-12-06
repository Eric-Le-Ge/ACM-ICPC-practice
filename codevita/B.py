N = int(input())
walls = []
for i in range(N):
	walls.append(input().replace(' ', ''))
ls = [w.count('C') for w in walls]
tops = [0] * N
for i in range(N):
	for w in walls:
		if w[i] == 'C':
			tops[i] += 1
# print(walls)
# print(ls, tops)
def maxAt(i, l):
	rmin = N - l[i]
	if rmin == 0:
		return 0
	res = 1
	while i < N - 1:
		i += 1
		rmin = min(rmin, N-l[i])
		if rmin > res:
			res += 1
		else:
			return res
	return res
resls = max([maxAt(i, ls) for i in range(N)])
restops = max([maxAt(i, tops) for i in range(N)])
res = max(resls, restops)
print(str(res), end='')
