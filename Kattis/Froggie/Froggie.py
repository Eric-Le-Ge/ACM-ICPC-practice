L, W = [int(_) for _ in raw_input().split()]
ois = []

def ok(pos, t):
	idx = pos[0]
	if idx == 0:
		return True
	idx -= 1
	rev = bool((idx + L + 1)%2)
	o, i, s = ois[idx]
	if not rev:
		closest = (o+t*s)%i - i
		while (closest + s) < pos[1]:
			closest += i
		return not ((closest < pos[1] <= (closest + s)) or closest == pos[1] and s==0)
	if rev:
		o = W - 1 - o
		closest = (o-t*s)%i + 20*i
		while (closest - s) > pos[1]:
			closest -= i
		return not ((closest > pos[1] >= (closest - s)) or closest == pos[1] and s==0)

for i in range(L):
	ois.append([int(_) for _ in raw_input().split()])
ois = ois[::-1]
stc, inst = raw_input().split()
stc = int(stc)
pos = [0, stc]
t = 0
for c in inst:
	if c == 'U':
		pos[0] += 1
	elif c=='D':
		pos[0] -= 1
	elif c=='L':
		pos[1] -= 1
	elif c=='R':
		pos[1] += 1
	if pos[0] > L:
		print ('safe')
		exit() 
	if not ok(pos, t):
		print ('squish')
		exit()
	t += 1

print ('squish')