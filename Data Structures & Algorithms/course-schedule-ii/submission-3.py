class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initialize adjacency list and indegree array
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            indegree[v] += 1
            adj_list[u].append(v)
        
        # find all nodes with indegree 0 and add to queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # iterate through the queue
        res = []
        finished_courses = 0
        while q:
            # mark finished courses and add to result
            node = q.popleft()
            finished_courses += 1
            res.append(node)

            # traverse node's neighbors and decrement indegree count of each neighbor
            for neigh in adj_list[node]:
                indegree[neigh] -= 1

                # if the neighbor has an indegree of 0 now, add it to the queue
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if finished_courses != numCourses: return []
        return res[::-1]