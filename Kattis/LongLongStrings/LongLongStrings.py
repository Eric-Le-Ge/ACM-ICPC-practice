
one = []
two = []

def format(lst):
	pt = 0
	while pt < len(lst) - 1:
		if lst[pt+1][1] and lst[pt][0] + 1 == lst[pt+1][0]: 
			while lst[pt][2]:
				lst[pt+1][2].insert(0, lst[pt][2].pop())
		pt += 1
	pt = 0
	while pt < len(lst):
		if lst[pt][1] == 0 and not lst[pt][2]:
			lst.pop(pt)
		pt += 1

def runD(ind, lst):
	idx = 0
	while idx < len(lst):
		before, after = lst[idx][0], lst[idx][0] + len(lst[idx][2]) - lst[idx][1]
		if ind > after:
			ind -= len(lst[idx][2]) - lst[idx][1]
		elif ind < before:
			lst.insert(idx, (ind, 1, []))
			return
		else:
			if ind + lst[idx][1] - 1 - before >= 0:
				lst[idx][2].pop(ind + lst[idx][1] - 1 - before)
			else:
				lst[idx] = (lst[idx][0], 1, lst[idx][2])
			if not lst[idx][2] and not lst[idx][1]:
				lst.pop(idx)
			return
		idx += 1
	lst.append((ind, 1, []))

def runI(ind, c, lst):
	idx = 0
	ind -= 1
	while idx < len(lst):
		before, after = lst[idx][0], lst[idx][0] + len(lst[idx][2]) - lst[idx][1]
		if ind > after:
			ind -= len(lst[idx][2]) - lst[idx][1]
		elif ind < before:
			lst.insert(idx, (ind, 0, [c]))
			return
		else:
			lst[idx][2].insert(ind + lst[idx][1] - before, c)
			return
		idx += 1
	lst.append((ind, 0, [c]))

for lst in (one, two):
	op = raw_input()
	while op != 'E':
		if op[0] == 'D':
			ind = int(op.split()[1])
			runD(ind, lst)

		elif op[0] == 'I':
			ind, c = int(op.split()[1]), op.split()[2]
			runI(ind, c, lst)
		op = raw_input()
format(one)
format(two)
if one == two:
	print(0)
else:
	print(1)