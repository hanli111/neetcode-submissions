class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p, s in zip(position, speed):
            pairs.append((p, s))
        pairs.sort(reverse=True)

        stk = []
        for p, s in pairs:
            stk.append((target - p) / s)
            # checks if a car will catch up to another car
            # if it does, we can pop the faster car since
            # it will catch the slower car and match its speed
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        return len(stk)


        '''
        [(4, 2), (1, 3)] target = 10

        (10-1)/3=3, (10-2)/4=2
        2 <= 3, pop
        stk = [3]
        return len(stk)
        '''