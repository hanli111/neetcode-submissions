class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 0
        while numbers[l] + numbers[r] != target:
            r += 1
            if r == len(numbers):
                r = 0
                l += 1
        return [min(l + 1, r + 1), max(l + 1, r + 1)]

        '''
         0  1  2  3
        [1, 2, 3, 4]  target = 3 -> return [1, 2] since 1-indexed
        
            R

         0   1   2   3
        [12, 13, 54, 58]  target = 112 -> return [3, 4]
                     L
                 R

         0  1  2
        [2, 3, 4]   target = 6 -> return [1, 3]
         L
               R
    
        l = 0
        r = 0
        while nums[l] + nums[r] != target
            r += 1
            if r == len(nums)
                r = 0
                l += 1
        return [min(l + 1, r + 1), max(l + 1, r + 1)]

        
        '''