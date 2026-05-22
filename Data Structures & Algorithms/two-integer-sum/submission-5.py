class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return [mapping[diff], i]
            mapping[n] = i
        
        '''
        nums = [3,4,5,6] target = 7
        mapping = {}

        i = 0, n = 3, diff = 4
        mapping = {3: 0}

        i = 1, n = 4, diff = 3
        diff is in mapping, so return [0, 1]
        '''