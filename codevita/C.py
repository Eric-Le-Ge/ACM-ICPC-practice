N = int(input())
s = input()
N = len(s)
res = set()
# do first substring
start, end = 0, 0
cur = ''
curind = start
while curind < N and s[curind] not in cur:
	cur += s[curind]
	curind += 1
res.add(cur)
end = curind
for start in range(1, N):
	cur = ''
	curind = start
	while curind < N and s[curind] not in cur:
		cur += s[curind]
		curind += 1
	#print(start, cur, curind, end)
	if (curind < N and cur[0] == s[curind]) or curind == end: # broken by first or proper
		end = max(end, curind)
		continue
	#print("added ", cur)
	end = max(end, curind)
	res.add(cur)
print(" ".join(sorted(res)), end='')
