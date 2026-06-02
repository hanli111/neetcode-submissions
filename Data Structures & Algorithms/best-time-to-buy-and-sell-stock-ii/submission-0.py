class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
    
        '''
        [7, 1, 5, 3, 6, 4]

        buy only if you can make profit

        |
        | 7
        |                   6
        |         5
        |                          4 
        |              3
        |
        |     1 
        |____________________________

        for i in range from 1 to len - 1
            if prices[i] > prices[i-1]
                profit = prices[i] - prices[i-1]

        '''