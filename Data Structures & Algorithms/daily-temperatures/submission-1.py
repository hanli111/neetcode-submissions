class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][1]:
                stk_idx, _ = stk.pop()
                res[stk_idx] = i - stk_idx
            stk.append((i, t))
        return res

        '''
                    i,t
        temp = [30, 38, 30, 36, 35, 40, 28]
            stk_idx

        stk = [(0, 30), ] (index, temp)
        res = [0, 0, 0, 0, 0, 0, 0]

        go through temps with temp and idx
        '''
