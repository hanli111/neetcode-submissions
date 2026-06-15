class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            num_hours = 0
            k = l + ((r - l) // 2)
            for p in piles:
                num_hours += math.ceil(float(p) / k)
            if num_hours <= h:
                res = k
                r = k - 1
            else:
                # too slow so increase l
                l = k + 1
        return res

        '''
        piles = [25, 10, 23, 4], h = 4 -> return 25


        [4, 10, 23, 25]     min eating speed = 1, max = 25
            L   k    R


        k = l + ((r - l) // 2)
        for p in piles:
            num_hours = 0 += ceil(float(p) / k) -> 5
        if num_hours <= h:
            res = k
            r = k - 1
        else:
            # too slow so increase l
            l = k + 1
        '''