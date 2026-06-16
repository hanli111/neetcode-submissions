class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        # checks to see if the capacity can fit all weights
        # with # of ships (days)
        def can_fit(cap):
            cur_weight = cap
            num_ships = 1
            for w in weights:
                if cur_weight - w < 0:
                    num_ships += 1
                    if num_ships > days:
                        return False
                    # reset to be middle val
                    cur_weight = cap
                cur_weight -= w
            return True
        
        while l <= r:
            m = l + ((r - l) // 2)
            if can_fit(m):
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res


        '''
        Input: weights = [1,5,4,4,2,3], ships = 3

        L = 5, R = 19, M = 12 check if cap of 12 can fit all
        the weights in 3 ships

        yes, can fit in 2 ships, so we need to decrement R
        R = M - 1 = 12 - 1 = 11
        M = 8 check again.. yes can fit in 3 this time, so we
        can decrement R again

        R = M - 1 = 8 - 1 = 7
        M = 6 check again.. no need 4 ships, so increment L
        
        L = M + 1 = 6 + 1 = 7
        M = 7 check again.. no need 4 ships still, so increment L

        L = M + 1 = 7 + 1 = 8
        so 8 is our answer
        '''