class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res


        '''
        [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
               L                         
                              R
        
        l_max = max(0, 2) = 2 -> max(2, 0) = 2
        r_max = 1 -> max(1, 2) = 2 -> max(2, 3) = 3
        res = 2-2=0 -> 0 -> 0 -> 2-0=2

        res = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r
            if l_max < r_max
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res
        '''