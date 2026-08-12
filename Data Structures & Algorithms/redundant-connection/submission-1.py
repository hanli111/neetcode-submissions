class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * (len(edges) + 1)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1: q.append(neigh)
        
        for u, v in reversed(edges):
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]
        return []