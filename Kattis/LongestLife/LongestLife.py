from collections import deque
n, p, c = [int(_) for _ in input().split()]
ps = [(0, 1.0)]
for _ in range(p):
	t, x, y = [float(_) for _ in input().split()]
	q = x/y
	ps.append((t, q))
inf = int(10e24)
# index, q, start, end, t, height
dq = deque([[0, 1.0, 0, inf, 0, 0]])
acc = deque()
for i in range(1, len(ps)):
	t, q = ps[i]
	if q <= dq[-1][1]:
		continue
	while dq[0][3] < t:
		acc.append(dq.popleft())
	height = dq[0][5] + (t-dq[0][4])/dq[0][1] + c
	overtake = 0
	while dq:
		heightdiff = height - (dq[-1][5] + (t-dq[-1][4])/dq[-1][1])
		overtake = t + (heightdiff*dq[-1][1]*q)/(q-dq[-1][1])
		if overtake > dq[-1][2]:
			break
		dq.pop()
	if dq:
		dq[-1][3] = overtake
	dq.append([i, q, overtake, inf, t, height])
res = 0.0
acc.extend(dq)
n = float(n)
while n>0:
	cost = min(n, (acc[0][3]-acc[0][2])/acc[0][1])
	res += cost*acc[0][1]
	n -= cost
	acc.popleft()
print(res)
