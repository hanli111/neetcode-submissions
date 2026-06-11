class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1
        while self.stk and price >= self.stk[-1][0]:
            _, stk_span = self.stk.pop()
            span += stk_span
        self.stk.append((price, span))
        return span


        ''' 
        span = 1
        stk = [(100, 0)] (price, span)
        '''


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)