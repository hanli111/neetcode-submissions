class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        # build adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # build degree for each node and add leaf nodes to queue
        degree = {}
        leaves = deque()
        for src, neighbor in adj_list.items():
            degree[src] = len(neighbor)
            if len(neighbor) == 1: leaves.append(src)
        
        while leaves:
            if n <= 2: return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neigh in adj_list[node]:
                    degree[neigh] -= 1
                    if degree[neigh] == 1: leaves.append(neigh)