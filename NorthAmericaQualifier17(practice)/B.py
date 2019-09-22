n, m, f, s, t = [int(_) for _ in raw_input().split()]
from collections import defaultdict
to = defaultdict(list)
tof = defaultdict(list)
used0 = set()
used1 = set()
for i in range(m):
	line = [int(_) for _ in raw_input().split()]
	to[line[0]].append((line[1], line[2]))
	to[line[1]].append((line[0], line[2]))
for i in range(f):
	line = [int(_) for _ in raw_input().split()]
	tof[line[0]].append(line[1])
	
import heapq
hp0 = [(0,s)]
hp1 = []
while True:
	if not hp1 or hp0[0][0] <= hp1[0][0]:
		cost, node = heapq.heappop(hp0)
		if node in used0:
			continue
		if node == t:
			print(cost)
			exit()
		used0.add(node)
		for nextnode, addcost in to[node]:
			if nextnode not in used0:
				heapq.heappush(hp0, (cost+addcost, nextnode))
		for nextnode in tof[node]:
			if nextnode not in used0:
				heapq.heappush(hp1, (cost, nextnode))

	else:
		cost, node = heapq.heappop(hp1)
		if node in used1:
			continue
		if node == t:
			print(cost)
			exit()
		used1.add(node)
		for nextnode, addcost in to[node]:
			if nextnode not in used1:
				heapq.heappush(hp1, (cost+addcost, nextnode))

