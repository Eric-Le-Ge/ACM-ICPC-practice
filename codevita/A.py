l = input().split()
S, T, M = 0, 0, 0
if len(l) == 1:
    S = int(l[0])
    T = int(input())
    M = int(input())
elif len(l) == 3:
    S, T, M = [int(_) for _ in l]

def calc_forward(pos, t): # 1 indexed
	if t % 2 == 1: #odd turn
		if S % 2 == 1: #odd people
			if pos == S: # odd last no move
				return pos
			elif pos % 2 == 1:
				return pos + 1
			else:
				pos -= 1
				if pos <= 0:
					pos += S
				return pos
		else: # even people
			if pos % 2 == 1:
				pos += 1
				if pos > S:
					pos -= S
				return pos
			else:
				pos -= 1
				if pos <= 0:
					pos += S
				return pos
	# even turn
	if S % 2 == 1: #odd people
		if pos == 1:
			return pos
		elif pos % 2 == 0:
			return pos + 1
		else:
			return pos - 1
	# even people
	if pos % 2 == 1:
		pos -= 1
		if pos <= 0:
			pos += S
		return pos
	pos += 1
	if pos > S:
		pos -= S
	return pos

def calc_backward(pos, t):
	left = pos + 1
	right = pos - 1
	if left > S:
		left -= S
	if right <= 0:
		right += S
	leftf = calc_forward(left, t)
	rightf = calc_forward(right, t)
	if leftf == pos:
		return left
	elif rightf == pos:
		return right
	return pos

# get the final position of student of interest
start_pos = M
for t in range(1, T+1):
	start_pos = calc_forward(start_pos, t)
left = start_pos + 1
right = start_pos - 1
if left > S:
	left -= S
if right <= 0:
	right += S
for t in range(T, 0, -1):
	left = calc_backward(left, t)
	right = calc_backward(right, t)
print("{} {}".format(left, right), end="")
