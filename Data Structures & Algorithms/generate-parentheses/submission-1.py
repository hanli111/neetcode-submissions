class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stk = []
        def backtrack(num_open: int, num_close: int):
            # base cases
            if num_open == num_close == n:
                res.append("".join(stk))
                return
            
            if num_open < n:
                stk.append("(")
                backtrack(num_open + 1, num_close)
                stk.pop()
            if num_close < num_open:
                stk.append(")")
                backtrack(num_open, num_close + 1)
                stk.pop()
        backtrack(0, 0)
        return res