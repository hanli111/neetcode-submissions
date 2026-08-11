class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n: return False
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        visited.add(0)
        q = deque([(0, -1)]) # (node, parent)
        while q:
            node, parent = q.popleft()
            for neigh in adj_list[node]:
                if neigh == parent: continue
                if neigh in visited: return False
                q.append((neigh, node))
                visited.add(neigh)
        return len(visited) == n