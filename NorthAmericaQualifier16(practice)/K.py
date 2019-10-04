T = int(raw_input())
for t in range(T):
	l1, a1, l2, a2, lt, at = [int(_) for _ in raw_input().split()]
	res = []
	for i in range(1, 10001):
		reml, rema = lt - i*l1, at-i*a1
		if reml<0 or rema <0 or reml%l2:
			continue
		j = reml//l2
		if rema == a2*j:
			res.append((i, j))
	if not res or len(res) > 1:
		print('?')
	else:
		print(str(res[0][0]) + ' '+ str(res[0][1]))
