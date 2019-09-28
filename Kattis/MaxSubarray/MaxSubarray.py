import sys
sys.setrecursionlimit(5000)
n, k = [int(_) for _ in raw_input().split()]
arr = [int(_) for _ in raw_input().split()]
dp = {(0,0,0):0, (0,0,1):0}
neginf = -(10000000000000L)
#i j last: max for j subs in first i elemnets where last is used if last = 1 and not used if last = 0
def compute(i, j, last):
	if (i, j, last) in dp:
		return dp[(i, j, last)]
	if j > i:
		res = neginf
	elif j == 0:
		res = neginf if last else 0
	else:
		if not last:
			res = max(compute(i-1, j, 0), compute(i-1, j, 1))
		else:
			res = max(compute(i-1, j-1, 1), compute(i-1, j, 1), compute(i-1, j-1, 0)) + arr[i-1]
	dp[(i, j, last)] = res
	return res
res = max(compute(n, k, 1), compute(n, k, 0))
print (res)
	