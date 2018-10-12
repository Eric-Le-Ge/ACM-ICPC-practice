import sys
n = int(sys.stdin.readline())
elems = {}
inputs = []
m =0
res = "no tie"
win = False
for line in sys.stdin:
	line = line[:-2]
	if len(line) < 5:
		continue
	elem =  [int(e) for e in line.split(' ')]
	inputs.append(elem)

def check(a,b):
	match = 0
	used = [False, False, False, False, False]
	for x in range(5):
		for y in range(x,5):
			if a[x] == b[y] and not used[y]:
				used[y] = True
				match += 1
				break
	return match == 5

for i in range(n):
	if win:
		break
	start_line = i*5
	a0 = []
	a1 = []
	a2 = []
	a3 = []
	a4 = []
	for j in range(5):
		a0.append(inputs[start_line+j][0])
		a1.append(inputs[start_line+j][1])
		a2.append(inputs[start_line+j][2])
		a3.append(inputs[start_line+j][3])
		a4.append(inputs[start_line+j][4])
		sum_row = sum(inputs[start_line+j])
		if sum_row in elems:
			for l in elems[sum_row]:
				if check(l) and not win:
					win = True
					res = (l[5]+1) + " " + (i+1)
	for col in [a0,a1,a2,a3,a4]:
		sum_col = sum(col)
		if sum_col in elems:
			for c in elems[sum_col]:
				if check(c) and not win:
					win = True
					res = (c[5]+1) + " " + (i+1)
	for j in range(5):
		sum_row = sum(inputs[start_line+j])
		inputs[start_line+j].append(i)
		if sum_row in elems:
			elems[sum_row].append(inputs[start_line+j])
		else:
			elems[sum_row] = [inputs[start_line+j]]
	for col in [a0,a1,a2,a3,a4]:
		sum_col = sum(col)
		col.append(i)
		if sum_col in elems:
			elems[sum_col].append(col)
		else:
			elems[sum_col] = [col]
print(elems)
print res
