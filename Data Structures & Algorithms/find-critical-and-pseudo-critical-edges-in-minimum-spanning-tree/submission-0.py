class DSU:
    def __init__(self, n):
        self.parent = list(range(n)) # or [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # KRUSKAL'S ALGORITHM
        for i, e in enumerate(edges):
            e.append(i) # (v1, v2, w, i)
        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        dsu = DSU(n)
        for v1, v2, w, i in edges:
            if dsu.union(v1, v2):
                mst_weight += w
        
        critical, psuedo = [], []
        for n1, n2, e_weight, i in edges:
            weight = 0
            dsu = DSU(n)
            for v1, v2, w, j in edges:
                if i != j and dsu.union(v1, v2):
                    weight += w
            if max(dsu.size) != n or weight > mst_weight:
                critical.append(i)
                continue
            
            weight = e_weight
            dsu = DSU(n)
            dsu.union(n1, n2)
            for v1, v2, w, j in edges:
                if dsu.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                psuedo.append(i)

        return [critical, psuedo]