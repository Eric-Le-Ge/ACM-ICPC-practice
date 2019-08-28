n, p, c = [int(_) for _ in input().split()]
ps = [(0, 1.0)]
for _ in range(p):
	t, x, y = [float(_) for _ in input().split()]
	q = x/y
	ps.append((t, q))
inf = int(10e24)
dq = [[0, 1.0, 0, inf]]
for i in range(1, len(ps)):
	t, q = ps[i]
	if q <= dq[-1][1]:
		continue
	# while dq and dq[0][3] < t:
	# 	dq.pop(0)
	overtake = 0
	while dq:
		overtake = t + (c*dq[-1][1]*q)/(q-dq[-1][1])
		if overtake > dq[-1][2]:
			break
		dq.pop()
	if dq:
		dq[-1][3] = overtake
	dq.append([i, q, overtake, inf])
res = 0.0
n = float(n)
while n>0:
	cost = min(n, (dq[0][3]-dq[0][2])/dq[0][1])
	res += cost*dq[0][1]
	n -= cost
	dq.pop(0)
print(res)
