class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
                res = r
            else:
                l = m + 1
        return res

        '''
        l = 0
        r = 13
        m = 6

        36 > 13
        r = m - 1 = 5
        m = 2
        4 < 13

        l = m + 1 = 3
        m = 4
        '''