from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        requirement = n // 3
        hashmap = Counter(nums)
        res = []

        for key, val in hashmap.items():
            if val > requirement:
                res.append(key)
        return (res)
