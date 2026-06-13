class FreqStack:

    def __init__(self):
        self.stk = []
        self.freq = {} # maps (val, frequency)

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1

    def pop(self) -> int:
        # print("Dictionary: ", self.freq)
        # print("Stack: ", self.stk)

        max_freq = -1
        top_num = None
        for s in self.stk[::-1]:
            #print(s)
            # get freq
            freq = self.freq.get(s, 0)
            
            if freq > max_freq:
                max_freq = freq
                top_num = s
        #print(len(self.stk) - 1 - self.stk[::-1].index(top_num))
        num_idx = len(self.stk) - 1 - self.stk[::-1].index(top_num)
        self.freq[top_num] = self.freq.get(top_num, 0) - 1
        return self.stk.pop(num_idx)
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()