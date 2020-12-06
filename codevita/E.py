from collections import Counter

N = int(input())
raws = input().replace(' ', '').split('|')
# ambiguity: one infected or any infected?

position = {}
infected = set()
first_infected = 0
infect_counter = Counter()
arrived = {}
ids = []

first = True
for pt in raws:
	cadet, pos = pt.split(':')
	pos = int(pos)
	cadet = int(cadet)
	if first:
		first = False
		infected.add(cadet)
		first_infected = cadet
	ids.append(cadet)
	position[cadet] = pos

sorted_ids = sorted(ids)

def home(cadet):
	return sorted_ids.index(cadet) + 1

def row(pos):
	return (pos - 1) // N + 1

def col(pos):
	return (pos - 1) % N + 1

def canUp(pos, cadet):
	if pos - N == home(cadet):
		return True
	elif pos <= 2 * N:
		return False
	return up(pos) not in position.values()

def canLeft(pos):
	if pos % N == 1:
		return False
	return left(pos) not in position.values()

def canRight(pos):
	if pos % N == 0:
		return False
	return right(pos) not in position.values()

def cadetAt(pos):
	for k, v in position.items():
		if v == pos:
			return k
	return 0

def up(pos):
	return pos - N

def left(pos):
	return pos - 1

def right(pos):
	return pos + 1

def down(pos):
	return pos + N

def infect():
	newinf = []
	# Ambiguities: infect from home?
	for cadet in ids:
		if cadet in infected or position[cadet] == home(cadet):
			continue
		inf = False
		inf |= position[cadet] > 2 * N and cadetAt(up(position[cadet])) in infected
		inf |= pos % N != 1 and cadetAt(left(position[cadet])) in infected
		inf |= pos % N != 0 and cadetAt(right(position[cadet])) in infected
		inf |= cadetAt(down(position[cadet])) in infected

		if not inf:
			infect_counter[cadet] = 0
		else:
			infect_counter[cadet] += 1
		if infect_counter[cadet] == N:
			newinf.append(cadet)

	for new in newinf:
		infected.add(new)

it = 0

def move(cadet): # return 1 if moved, 0 otherwise
	#print(position.items())
	direction = col(home(cadet)) - col(position[cadet])
	if direction == 0: # up
		if canUp(position[cadet], cadet):
			position[cadet] = up(position[cadet])
			if position[cadet] == home(cadet):
				arrived[cadet] = it
			return 1
		# otherwise blocked
	elif direction < 0: # left
		if canLeft(position[cadet]):
			position[cadet] = left(position[cadet])
			return 1
		else:
			other = cadetAt(left(position[cadet]))
			# if other going right
			other_dir = col(home(other)) - col(position[other])
			if other_dir > 0 and other < cadet and canUp(position[cadet], cadet):
				position[cadet] = up(position[cadet])
				return 1
	else:
		if canRight(position[cadet]):
			position[cadet] = right(position[cadet])
			return 1
		else:
			other = cadetAt(right(position[cadet]))
			# if other going left
			other_dir = col(home(other)) - col(position[other])
			if other_dir < 0 and other < cadet and canUp(position[cadet], cadet):
				position[cadet] = up(position[cadet])
				return 1

	return 0

def print_infected():
	infected.remove(first_infected)
	to_print = []
	for cadet in ids:
		if cadet in infected:
			to_print.append(str(cadet))
	print(" ".join(to_print), end='')

no_move = 0
while True:
	moves = 0
	for cadet in sorted_ids:
		moves += move(cadet)
		infect()
		it += 1
	if moves == 0:
		no_move += 1
	if no_move == 255:
		print('Blocked')
		print_infected()
		exit()
	if len(arrived.keys()) == len(ids):
		break

max_p, max_it = 0, -1
for k, v in arrived.items():
	if v > max_it:
		max_p = k
		max_it = v

print(max_p)
print_infected()







