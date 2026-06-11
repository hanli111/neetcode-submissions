class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t == "+":
                stk.append(stk.pop() + stk.pop())
            elif t == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b - a)
            elif t == "*":
                stk.append(stk.pop() * stk.pop())
            elif t == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(float(b / a)))
            else:
                stk.append(int(t))
        return(stk[0])

        '''
        [1, 2, 3, +, 4, -, *] -> ((2+3)-4)*1

        stk = [1, 1]
        '''