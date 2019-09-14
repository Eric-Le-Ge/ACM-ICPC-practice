from collections import defaultdict
import sys
sys.setrecursionlimit(2500)
""" Usage:

>>> a = [[0,0],[0,1],[1,0],[1,1]]
>>> g = GFG(a)
>>> g.maxBPM()
(2, [2, 0])
"""
class GFG: 
    def __init__(self, ps):
        self.ps = ps
        self.left = len(ps)

    def bpm(self, u, matchR, seen):
        l, r = self.ps[u][0], self.ps[u][1]
        for v in (l*r, l+r, l-r): 
            if seen[v] == False: 
                seen[v] = True 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen): 
                    matchR[v] = u
                    return True
        return False
  
    # Returns maximum number of matching  
    def maxBPM(self): 
        matchR = defaultdict(lambda :-1)
        result = 0
        for i in range(self.left):
            seen = defaultdict(bool)
            if self.bpm(i, matchR, seen):
                result += 1
        return result, matchR

n = int(raw_input())
ps = []
for i in range(n):
    ps.append([int(_) for _ in raw_input().split()])
res = [None]*n
_, match = GFG(ps).maxBPM()
if _ < n:
    print ('impossible')
    exit()
for k in match:
    v = match[k]
    if ps[v][0]+ps[v][1] == k:
        res[v] = '{} + {} = {}'.format(ps[v][0], ps[v][1], k)
    elif ps[v][0]*ps[v][1] == k:
        res[v] = '{} * {} = {}'.format(ps[v][0], ps[v][1], k)
    else:
        res[v] = '{} - {} = {}'.format(ps[v][0], ps[v][1], k)
for line in res:
    print (line)

