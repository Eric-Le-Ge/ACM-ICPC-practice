T = int(raw_input())

def computeToLose(l):
	tmp = []
	for i in range(len(l)):
		tup = l[i]
		energy = max(0, tup[1]-tup[0]*tup[2]*(N-len(l)))
		lost = min(energy, tup[2]*tup[0])
		
		tmp.append([lost, energy, i])

	return tmp


def solve(tuples):
	ret = 0
	for j in range(N):
		tmp = sorted(computeToLose(tuples))
		ret += tmp[-1][1]
		tuples = tuples[:tmp[-1][2]]+tuples[tmp[-1][2]+1:]
	return ret

for t in range(T):
	N = int(raw_input())
	tuples = []
	for i in range(N):
		tuples.append([int(_) for _ in raw_input().split()])
	res = solve(tuples)
	print "Case #{}: {}".format(t+1, res)

