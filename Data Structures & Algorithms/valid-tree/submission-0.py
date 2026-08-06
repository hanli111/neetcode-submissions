class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node, parent):
            # there is a cycle
            if node in visited:
                return False
            else:
                visited.add(node)

                for neigh in adj_list[node]:
                    if neigh == parent:
                        continue
                    else:
                        if not dfs(neigh, node):
                            return False
                return True
        
        return dfs(0, -1) and n == len(visited)