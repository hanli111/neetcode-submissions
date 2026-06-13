# class FreqStack:

#     def __init__(self):
#         self.stk = []
#         self.freq = {} # maps (val, frequency)

#     def push(self, val: int) -> None:
#         self.stk.append(val)
#         self.freq[val] = self.freq.get(val, 0) + 1

#     def pop(self) -> int:
#         max_freq = -1
#         top_num = None
#         for s in self.stk[::-1]:
#             # get freq
#             freq = self.freq.get(s, 0)
            
#             if freq > max_freq:
#                 max_freq = freq
#                 top_num = s
#         num_idx = len(self.stk) - 1 - self.stk[::-1].index(top_num)
#         self.freq[top_num] = self.freq.get(top_num, 0) - 1
#         return self.stk.pop(num_idx)
        


# # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(val)
# # param_2 = obj.pop()

class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.heap = [] # (freq, index, val), need a max heap since python defaults to a min heap
        self.index = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()