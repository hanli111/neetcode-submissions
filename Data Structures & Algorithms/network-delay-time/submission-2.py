class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DIJKSTRA'S ALGORITHM
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        visited = set()
        min_heap = [(0, k)]
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited: continue
            visited.add(n1)
            time = w1

            for neigh, w2 in adj_list[n1]:
                if neigh not in visited:
                    heapq.heappush(min_heap, (w1 + w2, neigh))
        
        return time if len(visited) == n else -1