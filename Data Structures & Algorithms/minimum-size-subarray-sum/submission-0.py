class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        cur_sum = 0
        min_len = float('inf')
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len

        '''
         0  1  2  3  4  5
        [2, 1, 5, 1, 5, 3]      target = 10
                  L
                     R
        for r in range()
            cur_sum = 0 -> 2, 3, 8, 9, 14; 6+3=8
            while cur_sum >= target
                min_len = min(r-l+1, min_len) -> 3
                cur_sum -= nums[l] -> 12 -> 11 -> 6
                l += 1
        '''
