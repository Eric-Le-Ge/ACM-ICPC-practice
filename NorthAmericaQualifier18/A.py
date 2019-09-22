n = int(raw_input())
from collections import defaultdict
adds = defaultdict(list)
cnts = [0]*500
rows = []
for i in range(n):
	for r in range(5):
		row = [int(_) for _ in raw_input().split()]
		rows.append(set(row))
		for e in row:
			adds[e].append(i*5+r)
	if i < n-1:
		raw_input()

def inject(un, sec):
	for e in un - sec:
		for target in adds[e]:
			cnts[target]+=1
			if cnts[target]==5:
				return False
	for j in list(sec):
		win = True
		sec.remove(j)
		for k in sec:
			for target in adds[k]:
				cnts[target]+=1
				if cnts[target]==5:
					win = False
		if win:
			return True
		for k in sec:
			for target in adds[k]:
				cnts[target]-=1
		sec.add(j)
	return False

for i in range(n*5-1):
	for j in range((i//5+1)*5, n*5):
		un, sec = rows[i] | rows[j], rows[i] & rows[j]
		cnts = [0]*500
		if inject(un, sec):
			print (str(i//5 + 1)+' '+str(j//5+1))
			exit()
print('no ties')

