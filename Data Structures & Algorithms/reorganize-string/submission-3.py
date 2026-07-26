class Solution:
    def reorganizeString(self, s: str) -> str:
        # maps letter to frequency of letter
        # "abbccdd"
        # [ {b : 2, c : 2, d : 2, a : 1} ]
        freq = Counter(s)
        max_heap = [[freq, letter] for letter, freq in freq.items()]
        heapq.heapify_max(max_heap)

        res = []
        prev = None

        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            freq, letter = heapq.heappop_max(max_heap)
            res += letter
            freq -= 1

            if prev:
                heapq.heappush_max(max_heap, prev)
                prev = None
            
            if freq > 0:
                prev = [freq, letter]
        return "".join(res)