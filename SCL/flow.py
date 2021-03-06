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


""" Max FLow (FordFulkerson)
Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
Usage:
>>> graph = [[0, 16, 13, 0, 0, 0], 
            [0, 0, 10, 12, 0, 0], 
            [0, 4, 0, 0, 14, 0], 
            [0, 0, 9, 0, 0, 20], 
            [0, 0, 0, 7, 0, 4], 
            [0, 0, 0, 0, 0, 0]]
>>> g = Graph(graph) 
>>> source = 0; sink = 1
>>> print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink)) 
"""
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self.ROW = len(graph) 

    def BFS(self,s, t, parent): 
        visited =[False]*(self.ROW) 
        queue=[] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            u = queue.pop(0) 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        return True if visited[t] else False

    def FordFulkerson(self, source, sink): 
        parent = [-1]*(self.ROW) 
        max_flow = 0
        while self.BFS(source, sink, parent) : 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
            max_flow +=  path_flow 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
        return max_flow

