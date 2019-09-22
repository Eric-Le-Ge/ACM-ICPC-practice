import sys
from collections import defaultdict
sys.setrecursionlimit(1001)
n = int(raw_input())
folo = defaultdict(list)
dp0 = {}
dp1 = {}
name2num = {}
speeds = {}
def helper(person, cov):
	if cov == 0:
		if person in dp0:
			return dp0[person]
		cnt, spd = 0, 0.0
		anss = []
		for f in folo[person]:
			anss.append(helper(f, 0))
		mgain = 0.0
		mgcnt = 0
		mj = -1
		for j in range(len(folo[person])):
			f = folo[person][j]
			ans = helper(f, 1)
			gain = ans[1] - anss[j][1] + min(speeds[person], speeds[f])*2
			if ans[0] + 1 >= anss[j][0]:
				gcnt = ans[0] - anss[j][0] + 1
				if gcnt > mgcnt:
					mgcnt = gcnt
					mgain = gain
					mj = j
				elif gcnt == mgcnt:
					if gain >= mgain:
						mgain = gain
						mj = j
		cnt = sum([k[0] for k in anss]) + mgcnt
		spd = mgain + sum([k[1] for k in anss])
		dp0[person] = (cnt, spd)
		return dp0[person]
	if cov == 1:
		if person in dp1:
			return dp1[person]
		cnt, spd = 0, 0.0
		for f in folo[person]:
			ans = helper(f, 0)
			cnt += ans[0]
			spd += ans[1]
		dp1[person] = (cnt, spd)
		return dp1[person]

people = []
for i in range(n):
	people.append(raw_input().split())
trak = 0
for person in people:
	person[1] = float(person[1])
	if person[0] in name2num:
		person[0] = name2num[person[0]]
	else:
		name2num[person[0]] = trak
		person[0] = trak
		trak += 1
	if person[2] in name2num:
		person[2] = name2num[person[2]]
	else:
		name2num[person[2]] = trak
		person[2] = trak
		trak += 1
for person in people:
	folo[person[2]].append(person[0])
	speeds[person[0]] = person[1]
c0, s0 = helper(name2num['CEO'], 1)
print(str(int(round(c0))) + ' ' +str(s0/(c0*2)))





