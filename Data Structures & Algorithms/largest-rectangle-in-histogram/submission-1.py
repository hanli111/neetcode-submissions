class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        


        '''

         _   _
        | | | | 
        | | | |
        | | | |    _
        | | | |   | |
        | | | |_ _| |
        | |_| | | | |
        |_|_|_|_|_|_|
             i
             h
            st

        [7,1,7,2,2,4]
        
        best_area = -1
        stk = [(1, 1)] (idx, height)

            idx = 2, height = 7
            best_area = max(7, height * (i - idx)) = 7

        '''