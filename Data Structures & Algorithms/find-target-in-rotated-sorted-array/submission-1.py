class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1
        
        # set bounds for binary search
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        # perform binary search on subarray
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


        '''
         0  1  2  3  4  5
        [3, 4, 5, 0, 1, 2], target = 1 -> return 4
                  L
                     M    
                        R
                  P

        split into 2 sub arrays, pivot at idx 4

        [3, 4, 5, 6] and [1, 2] find which subarray target belongs

        perform binary search on that subarray to see
        if target is in it or not

        '''