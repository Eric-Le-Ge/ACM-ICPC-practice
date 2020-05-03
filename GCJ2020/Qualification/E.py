""" Bipartite Matching
Usage:
>>> a = [[1,1,1],[0,0,0],[1,0,1],[1,1,0]]
>>> g = GFG(a)
>>> g.maxBPM()
(3, [3, 0, 2])

Note: Max independent set = number of vertices - maximum matching
"""
class GFG:
    def __init__(self,graph):
        self.graph = graph
        self.left = len(graph)
        self.right = len(graph[0])

    def bpm(self, u, matchR, seen):
        for v in range(self.right):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        matchR = [-1] * self.right
        result = 0
        for i in range(self.left):
            seen = [False] * self.right
            if self.bpm(i, matchR, seen):
                result += 1
        return result, matchR

def btFill(diagonal):
    n = len(diagonal)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = diagonal[i]

    def ok(i, j, num):
        for x in range(n):
            if matrix[i][x] == num:
                return False
        for y in range(n):
            if matrix[y][j] == num:
                return False
        return True

    def fillrow(i):
        graph = [[0]*n for _ in range(n)]
        for j in range(n):
            if matrix[i][j]:
                continue
            for num in range(1, n+1):
                if ok(i, j, num):
                    graph[num-1][j] = 1

        g = GFG(graph)
        ret = g.maxBPM()[1]
        for j in range(n):
            if not matrix[i][j]:
                matrix[i][j] = ret[j] + 1

    for i in range(n):
        fillrow(i)

    return matrix

T = int(input())

for t in range(1, T+1):
    N, K = [int(_) for _ in input().split()]
    diag = [1] * N
    if K == N+1 or K == N*N-1 or K > N*N:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue
    done = False

    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                if b==c and a!=b and N==3:
                    continue
                if b!=a and c!=a and a*N-2*a+b+c == K:
                    diag = [b]+[c]+[a]*(N-2)
                    done = True
                    break
                if a==b==c and a*N == K:
                    diag = [b]+[c]+[a]*(N-2)
                    done = True
                    break
            if done:
                break
        if done:
            break
    if N==2:
        if K==4:
            diag = [2,2]
        elif K==2:
            diag = [1,1]
        else:
            print("Case #{}: IMPOSSIBLE".format(t))
            continue
    if not done:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue
    res = btFill(diag)
    if not res:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        print("Case #{}: POSSIBLE".format(t))
        for row in res:
            print(" ".join([str(_) for _ in row]))
