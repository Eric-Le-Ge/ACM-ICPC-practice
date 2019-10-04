line = raw_input()
import math
if len(line) <= 158:
	num = int(line)
	for i in range(1, 101):
		if math.factorial(i) == num:
			print(i)
			exit()
cumu = 0.0
n = len(line)
for i in range(1, 210000):
	cumu += math.log(i, 10)
	if n == math.ceil(cumu):
		print(i)
		exit()
1/0
