import math
d, s = [float(_) for _ in input().split()]
def compute(a):
	return a*math.cosh(d/(2*a)) - a
a = 140000.0
step = 0.1
for _ in range(10):
	while a > 0 and compute(a) < s:
		if a > 20 and compute(a-10) < s:
			a -= 10
		a -= step
	a += step
	step /= 10
print (2*a*math.sinh(d/(2*a)))