class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, total, combo):
            # base cases
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # include nums[i]
            combo.append(nums[i])
            backtrack(i, total + nums[i], combo)

            # exclude nums[i]
            combo.pop()
            backtrack(i + 1, total, combo)
        
        backtrack(0, 0, [])
        return res