class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            indegree[v] += 1
            adj_list[u].append(v)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        finished_courses = 0
        while q:
            node = q.popleft()
            finished_courses += 1
            res.append(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if finished_courses != numCourses: return []
        return res[::-1]