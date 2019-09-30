import sys
lines = list(sys.stdin)[::-1]
t = 0

def solve(asofar, bsofar, bit, nextp):
	global gres
	if len(asofar) and len(asofar)==len(bsofar) and asofar == bsofar:
		if not gres:
			gres = asofar
			return
		if len(asofar) > len(gres):
			return
		if len(asofar) == len(gres) and asofar >= gres:
			return 
		gres = asofar
		return
	for i in range(n):
		if not (bit & 1<<i):
			tmpa, tmpb = asofar + awords[i], bsofar + bwords[i]
			if tmpa[:min(len(tmpa), len(tmpb))] == tmpb[:min(len(tmpa), len(tmpb))]:
				nextp.add((tmpa, tmpb, bit | 1<<i))

while lines:
	t += 1
	n = int(lines.pop())
	awords = []
	bwords = []
	for _ in range(n):
		a, b = lines.pop().split()
		awords.append(a)
		bwords.append(b)
	gres = None
	np = set([('', '', 0)])
	res = None
	for _ in range(n+1):
		p = set()
		for params in np:
			solve(params[0], params[1], params[2], p)
		np = p

	if not gres:
		gres = 'IMPOSSIBLE'
	print ('Case {}: {}'.format(t, gres))