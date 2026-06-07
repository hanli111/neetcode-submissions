class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        k = k % len(nums)

        # reverse nums -> [-3, 4, 2, 1000]
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # reverse first k nums -> [4, -3, 2, 1000]
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        # reverse last k nums -> [4, -3, 1000, 2]
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


        '''
        nums = [1000, 2, 4, -3], k = 2

        nums becomes [4, -3, 1000, 2]

          0    1  2   3
        [1000, 2, 4, -3]
          i

         0  1    2    3
        [4, -3, 1000, 2]
                 l
                         i 

        l = 0
        for i in range(len(nums)):
            if l + k > len(nums) - 1:
                l = (i + k) % len(nums)

            nums[i], nums[l + k] = nums[l + k], nums[i]
            l += 1

        nums = [1,2,3,4,5,6,7,8], k = 4

         0  1  2  3  4  5  6  7
        [5, 2, 3, 4, 1, 6, 7, 8]
         l
         i


        '''