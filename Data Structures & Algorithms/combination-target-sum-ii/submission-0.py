class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, total, combo):
            # base cases
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(candidates) or total > target:
                return

            combo.append(candidates[i])
            backtrack(i + 1, total + candidates[i], combo)

            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total, combo)
        
        backtrack(0, 0, [])
        return res