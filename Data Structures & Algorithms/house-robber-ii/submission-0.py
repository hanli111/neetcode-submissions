class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # partition first part
        arr1 = nums[:n-1]
        print(arr1)
        n1 = len(arr1)
        dp1 = [0] * (n1)

        # partition second part
        arr2 = nums[1:]
        n2 = len(arr2)
        dp2 = [0] * (n2)

        dp1[0] = arr1[0]
        dp1[1] = max(arr1[0], arr1[1])

        dp2[0] = arr2[0]
        dp2[1] = max(arr2[0], arr2[1])

        for i in range(2, n1):
            dp1[i] = max(arr1[i] + dp1[i-2], dp1[i-1])
            dp2[i] = max(arr2[i] + dp2[i-2], dp2[i-1])

        # return the max of each dp's last element
        return max(dp1[-1], dp2[-1])
