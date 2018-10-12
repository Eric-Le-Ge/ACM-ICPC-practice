class DisjointSet:
    size = 0
    par = []
    Rank = []

    def __init__(self, size):
        self.size = size
        for i in range(size):
            self.Rank.append(0)
            self.par.append(i)

    def find(self, x):
        if self.par[x]==x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.Rank[x]<self.Rank[y]:
            self.par[x]=y
        else:
            self.par[y] = x
            if self.Rank[x]==self.Rank[y]:
                 self.Rank[x]+=1
    def same(self, x, y):
        return self.find(x) == self.find(y)
