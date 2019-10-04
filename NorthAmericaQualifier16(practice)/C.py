import heapq
n = int(raw_input())
t = [int(_) for _ in raw_input().split()]
E = int(raw_input())
edges = [[] for _ in range(n)]
for i in range(E):
	a, b, d = [int(_) for _ in raw_input().split()]
	edges[a-1].append((b-1, d))
	edges[b-1].append((a-1, d))
used = set()
q = [(0, 0, -t[0])]
while q:
	d, node, cost = heapq.heappop(q)
	if node in used:
		continue
	used.add(node)
	if node == n-1:
		print (str(d) + ' ' + str(-cost))
		exit()
	for dest, dplus in edges[node]:
		if dest not in used:
			heapq.heappush(q, (d+dplus, dest, cost-t[dest]))
print ('impossible')