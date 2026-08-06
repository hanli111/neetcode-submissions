class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stk = []

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stk.append((start, h))

        for i, h in stk:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area