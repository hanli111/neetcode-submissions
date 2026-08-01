class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palidrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i: int, substr: List[str]):
            # base case
            if i == len(s):
                res.append(substr.copy())
                return
            
            for j in range(i, len(s)):
                if is_palidrome(s, i, j):
                    substr.append(s[i : j + 1])
                    backtrack(j + 1, substr)
                    substr.pop()
        
        backtrack(0, [])
        return res

            
