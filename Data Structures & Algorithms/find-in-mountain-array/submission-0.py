class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak
        length = mountainArr.length()
        l, r = 1, length - 2
        while l <= r:
            m = l + ((r - l) // 2)
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right:
                # search right
                l = m + 1
            elif left > mid > right:
                # search left
                r = m - 1
            else:
                break
        peak = m

        # perform BS on left side
        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        # perform BS on right side
        l, r = peak, length - 1
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        # not found
        return -1


    '''
    [1, 2, 3, 4, 2, 1]
     l
                    r
           m
    '''