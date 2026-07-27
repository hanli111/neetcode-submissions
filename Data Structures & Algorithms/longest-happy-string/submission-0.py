class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for freq, letter in [(a, "a"), (b, "b"), (c, "c")]:
            if freq > 0:
                heapq.heappush_max(max_heap, (freq, letter))
        
        res = ""
        while max_heap:
            # get the frequency and letter
            freq, letter = heapq.heappop_max(max_heap)

            # check if the result's last letter and second to letter letter are the same
            # and are equal to the currently popped letter
            if len(res) > 1 and res[-1] == res[-2] == letter:
                if not max_heap:
                    break
                
                # get the second highest frequency and letter and add to result
                freq2, letter2 = heapq.heappop_max(max_heap)
                res += letter2
                freq2 -= 1
                if freq2 > 0:
                    heapq.heappush_max(max_heap, (freq2, letter2))
                
                # remember to add back the highest frequency and letter
                heapq.heappush_max(max_heap, (freq, letter))
            # otherwise we can just add the letter to result
            else:
                res += letter
                freq -= 1
                if freq > 0:
                    heapq.heappush_max(max_heap, (freq, letter))
        return res