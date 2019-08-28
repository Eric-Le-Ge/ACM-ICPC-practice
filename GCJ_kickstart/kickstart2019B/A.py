T = int(raw_input())


for t in range(T):
	N, Q = [int(_) for _ in raw_input().split()]
	line = raw_input()
	Res = 0

	rstats = [0] * 26
	stats = []
	for i in range(N):
		rstats[ord(line[i])-ord('A')] += 1
		tmp = [num for num in rstats]
		stats.append(tmp)
	for i in range(Q):
		start, end = [int(_) for _ in raw_input().split()]
		s = [0] * 26
		for j in range(26):
			s[j] += stats[end-1][j]
			if start > 1:
				s[j] -= stats[start-2][j]
		singles = 0
		for num in s:
			if num % 2!=0:
				singles += 1
		Res += singles < 2
	print "Case #{}: {}".format(t+1, Res)

