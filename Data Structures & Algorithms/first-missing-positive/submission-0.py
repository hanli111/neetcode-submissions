class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # in place cyclic sort 
        # element number must match where it goes
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue
            
            idx = nums[i] - 1
            if nums[i] != nums[idx]:
                # swap places with each other
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
            

        '''
                0  1  2  3  4  5  6
        nums = [1, 2, 3, 4, 5, 6, 1]
                                  i
                      idx = 6
                      1 !=

                      0  1  2  3  4  5  6
        turn it into [1, 2, 3, 4, 5, 6, 1]
        i + 1 must equal nums[i]
        if not, return i + 1
        else, return n + 1
        '''