class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set()
        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
        return False




        '''
         0  1  2  3
        [1, 2, 2, 3] k = 3
         L
               R

        set = (1, 2)
        j = 2, i = 1, abs(1-2) <= k is not true so return false

        '''