class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res

        '''
        |   *
        |
        |
        |                   *
        |               *
        |           *
        |
        |
        |       *               *
        |_______________________________

        buy low sell high
        [10, 1, 5, 6, 7, 1]
             L   
                R


        buy at 1, sell at 7, profit = 6
        
        '''