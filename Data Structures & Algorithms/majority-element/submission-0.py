class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = Counter(nums)
        return max(mapping, key=mapping.get)