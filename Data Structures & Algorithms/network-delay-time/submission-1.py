class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = set()
        time = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, w1)

            for n2, w2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w2 + w1, n2))
        
        return time if len(visited) == n else -1
