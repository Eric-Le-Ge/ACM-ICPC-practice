n = int(raw_input())
pts = []
for i in range(n):
    pts.append(tuple([int(_.replace('.','')) for _ in raw_input().split(' ')]))
res = 0
if len(set(pts)) == 1:
    print (n)
    exit()
for i in range(n-1):
    x0, y0 = pts[i]
    for j in range(i+1, n):
        x1, y1 = pts[j]
        if x0 == x1 and y0 == y1:
            continue
        dx, dy = x1-x0, y1-y0
        a, b, c = dy, -dx, -(dy*x0-dx*y0)
        tmp = 40000*(a*a+b*b)
        run0, run1 = 0, 0
        for k in range(n):
            x2, y2 = pts[k]
            run0 += ((a*x2+b*y2+c)**2 <= tmp and a*x2+b*y2+c >= 0)
            run1 += ((a*x2+b*y2+c)**2 <= tmp and a*x2+b*y2+c <= 0)
        res = max(res, run0, run1)
print (res)