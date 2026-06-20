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


    '''
    nums = [2, 4, 10, 1, 5], k = 2
                   n

    l = 10
    r = 22
    m = 16
    res = 22

    can_split(16)
        subarray = 1
        cur_sum = 0 -> 2 not greater than 16
        cur_sum = 6...16...17 is greater than 16
        subarray = 2 and cur_sum = 1
        cur_sum = 6
        return true since subarray <= k

    res = 16
    r = 15
    l = 10
    m = 12

    can_split(12)
        subarray = 1
        cur_sum = 0...2...6...16 is greater than 12
        subarray = 2 and cur_sum = 10
        cur_sum = 11...16 is greater than 12
        subarray = 3 so returns false
    
    l = 13
    r = 15
    m = 14

    can_split(14)
        return false

    l = 15, r = 15, m = 15
    can_split(15)
        return false
    l = 16, so return res = 16
    '''