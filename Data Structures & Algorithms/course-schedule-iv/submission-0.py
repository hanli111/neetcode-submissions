class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        KHAN'S ALGORITHM
        '''
        # is_prereq[i] means i has a prereq of ...
        is_prereq = [set() for _ in range(numCourses)]

        # must take course ai first if you want to take course bi
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            indegree[v] += 1
            adj_list[u].append(v)
        
        # add all indegrees of 0 to the queue
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: q.append(i)

        # iterate through the queue
        while q:
            node = q.popleft()

            # go through each node's neighbors
            for neigh in adj_list[node]:
                # add the neighbor's prereq to the set
                is_prereq[neigh].add(node)

                # if there's a chain of prereqs, add the other nodes too
                is_prereq[neigh].update(is_prereq[node])

                # decrement indegree for the neighbor and add to queue if indegree drops to 0
                indegree[neigh] -= 1
                if indegree[neigh] == 0: q.append(neigh)
        
        res = []
        for u, v in queries:
            if u in is_prereq[v]:
                res.append(True)
            else:
                res.append(False)
        return res