class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range (1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

        '''
        sliding window
         0  1  2  3  4  5
        [6, 6, 7, 7, 8, 9] -> return [6, 7, 8, 9] with k = 4
               L
               R

        for r in range 1, len(nums)
            if nums[r] != nums[r-1] -> not a dup
                nums[l] = nums[r]
                l += 1
        return l

        '''


