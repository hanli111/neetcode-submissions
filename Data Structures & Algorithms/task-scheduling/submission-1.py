from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        max_heap = [-count for count in hashmap.values()]
        heapq.heapify(max_heap)
        q = deque() # (count, idle time)
        time = 0 

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count != 0:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

