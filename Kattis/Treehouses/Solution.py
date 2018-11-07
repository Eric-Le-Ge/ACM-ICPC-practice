
INF = 0x3f3f3f3
n, e, p = [int(s) for s in input().split(' ')]
G = [0] * n
for i in range(n):
    G[i] = [INF] * n
mincost = [INF]*n
used = [False]*n
points = [[0,0]]*n
for i in range(n):
    points[i] = [float(s) for s in input().split(' ')]


for i in range(n):
    for j in range(i+1, n):
        G[i][j] = G[j][i] = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5

for i in range(e):
    for j in range(i+1, e):

        G[i][j] = G[j][i] = 0


for i in range(p):
    v1, v2 = [int(s) for s in input().split(' ')]
    G[v1-1][v2-1] = G[v2-1][v1-1] = 0

mincost[0] = 0
res = 0

while True:
    v = -1
    for u in range(n):
        if (not used[u]) and (v==-1 or mincost[u] < mincost[v]):
            v = u
    if v == -1:
        break
    used[v] = True
    res+=mincost[v]
    for u in range(n):
        mincost[u] = min(mincost[u], G[v][u])

print(res)
