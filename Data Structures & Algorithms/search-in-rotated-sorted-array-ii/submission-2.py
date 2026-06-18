class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return True

            if nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] < nums[m]:
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1
        return False


        '''
                0  1  2  3  4  5  6
        nums = [2, 5, 6, 7, 0, 1, 2], target = 6
                L         
                                  R
                         M
        '''