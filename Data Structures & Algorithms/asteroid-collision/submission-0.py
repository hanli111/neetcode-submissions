class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            # make sure asteroids can collide
            while stk and a < 0 and stk[-1] > 0:
                diff = a + stk[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stk.pop()
                else:
                    a = 0
                    stk.pop()

            if a != 0:
                stk.append(a)

        return stk

        '''
                    a
        [2, 4, -4, -1]

        stk = [2]
        '''