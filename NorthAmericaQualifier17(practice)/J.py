t = int(raw_input())
for i in range(t):
	line = raw_input()
	a = line[0]
	line = line[2:]
	if a == 'e':
		run = 0
		runs = []
		for c in line:
			if c!=' ':
				run += ord(c) - ord('a') + 1
			runs.append(run)
		runs = map(lambda x: x%27, runs)
		runs = map(lambda x: chr(x-1+ord('a')) if x>0 else ' ', runs)
		print ("".join(runs))
	else:
		runs = []
		for c in line:
			runs.append(ord(c)-ord('a') + 1 if c!=' ' else 0)
		diffs = [runs[0]]
		for j in range(len(runs)-1):
			diffs.append((runs[j+1]-runs[j]+27)%27)
		diffs = map(lambda x: chr(x+ord('a')-1) if x>0 else ' ', diffs)
		print("".join(diffs))

