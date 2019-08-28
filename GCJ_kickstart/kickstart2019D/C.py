import bisect
T = int(raw_input())

def solve():
	N, G, M = [int(_) for _ in raw_input().split()]
	creg = {}
	cregm = {}
	areg = {}
	aregm = {}
	cpos = set()
	apos = set()
	for i in range(G):
		pos, d = raw_input().split()
		pos = int(pos)
		if d == 'C':
			pos = (pos-1+M)%N
			if pos in creg:
				creg[pos].append(i)
			else:
				creg[pos]=[i]
				cpos.add(pos)
		if d == 'A':
			pos = (pos-1-M)%N
			if pos in areg:
				areg[pos].append(i)
			else:
				areg[pos]=[i]
				apos.add(pos)
	cpos = sorted(list(cpos))
	apos = sorted(list(apos))
	acum = [0]*G
	for n in range(N):
		crem, arem = -1, -1
		if cpos:
			ctmp = bisect.bisect_left(cpos, n)
			crem = cpos[ctmp] - n if ctmp < len(cpos) else N-n+cpos[0]
		if apos:
			atmp = bisect.bisect_right(apos, n)
			arem = n-apos[atmp-1] if atmp>0 else N-apos[-1]+n
		if (min(crem, arem)>M) or (arem==-1 and crem>M) or (crem==-1 and arem>M):
			continue
		#print n, arem, crem, apos, cpos
		if crem == arem:
		    if (n+crem)%N in cregm:
		        cregm[(n+crem)%N]+=1
		    else:
		    	cregm[(n+crem)%N]=1
		    if (n-arem)%N in aregm:
		    	aregm[(n-arem)%N]+=1
		    else:
		    	aregm[(n-arem)%N]=1
		elif crem == -1:
			if (n-arem)%N in aregm:
				aregm[(n-arem)%N]+=1
			else:
			    aregm[(n-arem)%N]=1
		elif arem == -1 or crem < arem:
			if (n+crem)%N in cregm:
				cregm[(n+crem)%N]+=1
			else:
				cregm[(n+crem)%N]=1
		else:
			if (n-arem)%N in aregm:
				aregm[(n-arem)%N]+=1
			else:
				aregm[(n-arem)%N]=1
	for k, v in cregm.items():
		for i in creg[k]:
			acum[i]+=v
	for k, v in aregm.items():
		for i in areg[k]:
			acum[i]+=v
	return acum
	


for t in range(T):
	res = solve()
	print "Case #{}: {}".format(t+1, " ".join(map(str,res)))