class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        # [to, capacity]
        min_heap = []
        cur_capacity = 0

        for cap, start, to in trips:
            while min_heap and min_heap[0][0] <= start:
                cur_capacity -= heapq.heappop(min_heap)[1]

            cur_capacity += cap
            if cur_capacity > capacity:
                return False
            
            heapq.heappush(min_heap, (to, cap))
        
        return True
        

