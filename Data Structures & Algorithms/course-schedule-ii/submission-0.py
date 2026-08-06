class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)

        order = []
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            #state = states[node]
            # there's a cycle
            if states[node] == VISITING:
                return False
            # no cycle
            elif states[node] == VISITED:
                return True
            # not visited yet, so we need to visit it
            else:
                states[node] = VISITING

                # go through all the neighbors
                for neigh in adj_list[node]:
                    if not dfs(neigh):
                        return False
                
                states[node] = VISITED
                order.append(node)
                return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order