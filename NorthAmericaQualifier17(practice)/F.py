# d: 0: left, 1, up, 2, right, 3, down
tarx, tary = [int(_) for _ in raw_input().split()]
n = int(raw_input())
inst = []
for i in range(n):
	inst.append(raw_input())
cp, cd = (0, 0), 1
pos = [(0, 0)]
ds = [1]
for i in inst:
	if i == 'Forward':
		if cd == 0:
			cp = (cp[0]-1, cp[1])
		elif cd == 1:
			cp = (cp[0], cp[1]+1)
		elif cd == 2:
			cp = (cp[0]+1, cp[1])
		else:
			cp = (cp[0], cp[1]-1)
	elif i == 'Left':
		cd = (cd-1+4)%4
	else:
		cd = (cd+1)%4
	pos.append(cp)
	ds.append(cd)
tx, ty = pos[-1]
for i in range(1, n+1):
	bx, by = pos[i-1]
	ax, ay = pos[i]
	ins = inst[i-1]
	bd = ds[i-1]

	#print(bx, by, ax, ay, ins, bd)
	if ins == 'Right':
		#r 2 left
		dx, dy = tx-bx, ty-by
		if bx - dx == tarx and by - dy == tary:
			print (str(i) +' Left')
			exit()
		dx, dy = -dy, dx
		if bd == 0:
			bx -= 1
		elif bd == 1:
			by += 1
		elif bd == 2:
			bx += 1
		else:
			by -= 1
		if bx + dx == tarx and by + dy == tary:
			print (str(i) +' Forward')
			exit()
	elif ins == 'Left':
		#l 2 r
		dx, dy = tx-bx, ty-by
		if bx - dx == tarx and by - dy == tary:
			print (str(i) +' Right')
			exit()
		dx, dy = dy, -dx
		if bd == 0:
			bx -= 1
		elif bd == 1:
			by += 1
		elif bd == 2:
			bx += 1
		else:
			by -= 1
		if bx + dx == tarx and by + dy == tary:
			print (str(i) +' Forward')
			exit()
	else:
		dx, dy = tx-ax, ty-ay
		if bx - dy == tarx and by + dx == tary:
			print (str(i) +' Left')
			exit()
		if bx + dy == tarx and by - dx == tary:
			print (str(i) +' Right')
			exit()
