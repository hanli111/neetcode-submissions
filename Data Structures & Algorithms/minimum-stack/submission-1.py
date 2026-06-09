class MinStack:

    def __init__(self):
        # 2 stacks, main and min stack
        self.main_stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        # main stack would have every single element
        self.main_stk.append(val)

        # min stack would only have the minimum
        # so we append min(val, min_stk[-1])
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(val, self.min_stk[-1]))

    def pop(self) -> None:
        # we can pop from both
        self.main_stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        # we can simply return the top element from main stack
        return self.main_stk[-1]

    def getMin(self) -> int:
        # we can simply return the top element from min stack
        return self.min_stk[-1]
