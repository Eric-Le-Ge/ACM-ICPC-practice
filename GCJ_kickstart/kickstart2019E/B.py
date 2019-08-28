import bisect
def solve():
	D, S = [int(_) for _ in input().split()]
	days = []
	s = []
	for _ in range(S):
		s.append([int(_) for _ in input().split()])
	for _ in range(D):
		days.append([int(_) for _ in input().split()])
	s.sort(key=lambda x: float(x[0])/x[1] if x[1] else 100000)
	eatacc = []
	codeacc = []
	run = 0
	for p in s:
		run += p[1]
		eatacc.append(run)
	run = 0
	for p in s[::-1]:
		run += p[0]
		codeacc.append(run)
	codeacc = codeacc[::-1]
	res = ""
	for c, e in days:
		ind = bisect.bisect_left(eatacc, e)
		if ind == S:
			res += "N"
			continue
		rem = eatacc[ind]-e
		give = float(rem*s[ind][0])/s[ind][1] if s[ind][1] else s[ind][0]
		other = give + codeacc[ind+1] if ind+1<S else give
		if other >= c:
			res += "Y"
		else:
			res += "N"
	return res



T = int(input())
for t in range(1, T+1):
	res = solve()
	print("Case #{}: {}".format(t, res))