class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            else:
                states[node] = VISITING
            
                for neigh in adj_list[node]:
                    if not dfs(neigh):
                        return False
                
                states[node] = VISITED
                return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True