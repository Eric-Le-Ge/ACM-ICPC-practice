""" Usage:
>>> a = [[0,0],[0,1],[1,0],[1,1]]
>>> g = GFG(a)
>>> g.maxBPM()
(2, [2, 0])
"""

class GFG: 
    def __init__(self,graph): 
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0])

    def bpm(self, u, matchR, seen): 
        for v in range(self.jobs): 
            if self.graph[u][v] and seen[v] == False: 
                seen[v] = True 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
  
    # Returns maximum number of matching  
    def maxBPM(self): 
        matchR = [-1] * self.jobs 
        result = 0 
        for i in range(self.ppl): 
            seen = [False] * self.jobs 
            if self.bpm(i, matchR, seen): 
                result += 1
        return result, matchR

n, k = [int(_) for _ in raw_input().split()]
matrix = []
for i in range(k):
    matrix.append([int(_)-1 for _ in raw_input().split()])
    if len(set(matrix[i])) != n:
        print ('no')
        exit()
cans = [set(range(n))-set([row[i] for row in matrix]) for i in range(n)]
for c in cans:
    if len(c) != n-k:
        print ('no')
        exit()
for it in range(n-k):
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i in cans[j]:
                graph[i][j] = 1
    _, row = GFG(graph).maxBPM()
    for i in range(n):
        cans[i].remove(row[i])
    matrix.append(row)
print('yes')
for row in matrix:
    print(" ".join(map(lambda x: str(x+1), row)))
