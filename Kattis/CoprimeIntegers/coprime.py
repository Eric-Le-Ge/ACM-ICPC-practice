a,b,c,d = [int(s) for s in input().split(' ')]
maxV = min(b,d)+1
bad = [False]*maxV
p = [0]*maxV
for i in range(2,maxV):
    if p[i]: continue
    for j in range(i, maxV, i):
        p[j] += 1
    i2 = i*i
    if i2 < maxV:
        for k in range(i2,maxV, i2):
            bad[k] = True

def solve(a, b):
    ret = a*b
    for i in range(2,maxV):
        if bad[i]: continue
        tmp = (a//i) * (b//i)
        if p[i]&1:
            ret -= tmp
        else:
            ret += tmp
    return ret
print(solve(a-1,c-1)+solve(b,d)-solve(a-1,d)-solve(b,c-1))
