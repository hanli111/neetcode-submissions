class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # keep track of original index
        for i, t in enumerate(tasks):
            t.append(i)

        # sort by enq time
        tasks.sort(key = lambda t : t[0])

        res, min_heap = [], []

        # get current task index and first time
        i, time = 0, tasks[0][0]
        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                # add to heap the (proc time, original index)
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            # check if heap is empty
            if not min_heap:
                # advance the time
                time = tasks[i][0]
            # not empty
            else:
                # get proc time and original index from popping
                proc_time, idx = heapq.heappop(min_heap)
                res.append(idx)
                time += proc_time
        return res