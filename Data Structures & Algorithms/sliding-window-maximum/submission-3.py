class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # holds index
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            # check if window is big enough
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
        return res
        

        '''
         0  1  2  3  4
        [1, 3, 4, 2, 7]     k = 3
               L
                     R

        q = [4]
        res = [4, 4, 7]
        '''