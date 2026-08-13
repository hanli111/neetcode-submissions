class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj_list[a].append((b, values[i]))
            adj_list[b].append((a, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adj_list or target not in adj_list:
                return -1

            q = deque([(src, 1)])
            visited = set()
            visited.add(src)
            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for neigh, new_weight in adj_list[node]:
                    if neigh not in visited:
                        q.append((neigh, weight * new_weight))
                        visited.add(neigh)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]