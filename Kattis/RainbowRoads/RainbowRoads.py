
n = int(raw_input())
g = [[] for _ in range(n+1)]
bad = set([0])

for i in range(n-1):
	a, b, c = [int(_) for _ in raw_input().split()]
	g[a].append((b, c))
	g[b].append((a, c))

def color(v, p):
	stack = [(v, p)]
	while stack:
		v, p = stack.pop()
		if v in bad:
			continue
		m = {}
		parentcolor = -1
		for b, c in g[v]:
			if c in m:
				m[c].append(b)
			else:
				m[c] = [b]
			if b == p:
				parentcolor = c
		if parentcolor == -1:
			exit()
		if len(m[parentcolor]) > 1:
			return True
		bad.add(v)
		for nex, _ in g[v]:
			if nex != p and nex not in bad:
				stack.append((nex, v))
	return False

for i in range(1, n+1):
	m = {}
	for b, c in g[i]:
		if c in m:
			m[c].append(b)
		else:
			m[c] = [b]
	for c, l in m.items():
		if len(l) > 1:
			for v in l:
				if color(v, i):
					print (0)
					exit ()

res = set(range(n+1)) - bad
print (len(res))
for v in sorted(res):
	print (v)