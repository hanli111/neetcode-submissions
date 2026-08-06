class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        two_n = 2 * len(nums)
        n = len(nums)
        ans = [0] * two_n

        for i in range(two_n):
            ans[i] = nums[i % n]
        return ans

        '''
        nums = [1, 4, 1, 2]

        i =    0, 1, 2, 3, 4, 5, 6, 7
        ans = [1, 4, 1, 2, 1, 4, 1, 2]
        ans[i] = nums[i mod n]
        '''