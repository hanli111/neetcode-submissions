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

        def backtrack(i: int, j: int, substr: List[str]):
            # base case
            if j == len(s):
                if j == i:
                    res.append(substr.copy())
                return
            
            if is_palidrome(s, i, j):
                substr.append(s[i : j + 1])
                backtrack(j + 1, j + 1, substr)
                substr.pop()
            
            backtrack(i, j + 1, substr)
            return res
        
        backtrack(0, 0, [])
        return res

            
