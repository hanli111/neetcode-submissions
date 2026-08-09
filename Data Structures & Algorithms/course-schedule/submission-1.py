class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        visited = set()

        def dfs(node):
            # cycle detected
            if node in visited:
                return False
            if adj_list[node] == []:
                return True
            
            visited.add(node)
            
            for neigh in adj_list[node]:
                if not dfs(neigh):
                    return False
            
            visited.remove(node)
            adj_list[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True