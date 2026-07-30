class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, combo):
            if i > n:
                if len(combo) == k:
                    res.append(combo.copy())
                return
            
            combo.append(i)
            backtrack(i + 1, combo)
            combo.pop()
            backtrack(i + 1, combo)
        
        backtrack(1, [])
        return res