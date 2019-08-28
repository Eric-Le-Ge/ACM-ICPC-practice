import bisect
T = int(raw_input())

def  csb(n): 
	count = 0
	while (n): 
		count += n & 1
		n >>= 1
	return count%2

def solve():
	N, Q = [int(_) for _ in raw_input().split()]
	arr=[csb(int(_)) for _ in raw_input().split()]
	piv = 0
	res = []
	ones = []
	piv = sum(arr)
	for i in range(N):
		if arr[i]:
			ones.append(i)
	for i in range(Q):
		pos, num = [int(_) for _ in raw_input().split()]
		num = csb(num)
		if num == arr[pos]:
			pass
		elif num:
			arr[pos] = num
			piv += 1
			bisect.insort(ones, pos)
		else:
			arr[pos] = num
			piv -=1 
			del ones[bisect.bisect_left(ones, pos)]
		if piv %2==0:
			res.append(N)
		else:
			res.append(max(N-ones[0]-1, ones[-1]))
	return res

for t in range(T):
	res = solve()
	print "Case #{}: {}".format(t+1, " ".join(map(str,res)))