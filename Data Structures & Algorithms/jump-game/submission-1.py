class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 1, -1, -1):
            max_jumps = nums[i]
            if max_jumps + i >= goal:
                goal = i
        return goal == 0