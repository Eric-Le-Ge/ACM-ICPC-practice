n = int(raw_input())
lp, rp, res = {}, {}, 0
for i in range(n):
	l, r, h = [int(_) for _ in raw_input().split()]
	l, r = min(l, r), max(l, r)
	w = r-l
	lp[(l, h)] = w
	rp[(r, h)] = w
for x, y in list(lp.keys())+list(rp.keys()):
	rest = []
	for pt, w in lp.items():
		x0, y0 = pt
		if y0>y:
			rest.append(((x0-x)/float(y0-y), -w)) #float may break
		elif y0<y:
			rest.append(((x0-x)/float(y0-y), w))
	for pt, w in rp.items():
		x0, y0 = pt
		if y0>y:
			rest.append(((x0-x)/float(y0-y), w))
		elif y0<y:
			rest.append(((x0-x)/float(y0-y), -w))
	rest.sort()
	run = lp[(x, y)] if (x, y) in lp else rp[(x,y)]
	res = max(res, run)
	for i in range(len(rest)-1):
		run -= rest[i][1]
		res = max(res, run)
print (res)
