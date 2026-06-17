class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[m]


        '''
         0  1  2  3  4  5
        [4, 5, 0, 1, 2, 3] -> return 0
               L
               R
            M
        
        M = 2 -> 1
        check if nums[M] < nums[R]
            R = M
        else:
            L = M + 1
        '''