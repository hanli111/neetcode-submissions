from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra's algorithm
        INF = float("inf")
        adj_list = defaultdict(list)
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, w in flights:
            adj_list[u].append([v, w])

        dist[src][0] = 0
        min_heap = [(0, src, -1)]
        while min_heap:
            c, source, stops = heapq.heappop(min_heap)
            if dst == source: return c
            if stops == k or dist[source][stops + 1] < c:
                continue

            # go through every neighbor
            for neigh, w in adj_list[source]:
                next_cost = c + w
                next_stops = 1 + stops
                if dist[neigh][next_stops + 1] > next_cost:
                    dist[neigh][next_stops + 1] = next_cost
                    heapq.heappush(min_heap, (next_cost, neigh, next_stops))

        return -1