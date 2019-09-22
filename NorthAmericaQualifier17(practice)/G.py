s = set()
magic = [(0, 2018), (0, -2018), (-1118, 1680), (-1118, -1680), (1118, -1680), (1118, 1680),
(1680, 1118), (-1680, 1118), (1680, -1118), (-1680, -1118), (2018, 0), (-2018, 0)]
n = int(raw_input())
res = 0
for i in range(n):
	x, y = [int(_) for _ in raw_input().split()]
	for dx, dy in magic:
		if (x+dx, y+dy) in s:
			res += 1
	s.add((x, y))
print (res)