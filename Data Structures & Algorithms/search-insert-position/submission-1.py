class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l


        '''
         0   1  2  3  4  5
        [-1, 0, 2, 4, 6, 8], target = 5
                   L          
                      R
                      M

        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            if target not in nums:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] >= target:
                    r = m
        '''