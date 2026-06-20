class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest: int) -> bool:
            subarray = 1
            cur_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    subarray += 1
                    cur_sum = n
            return True if subarray <= k else False
        
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = l + ((r - l) // 2)
            if can_split(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res