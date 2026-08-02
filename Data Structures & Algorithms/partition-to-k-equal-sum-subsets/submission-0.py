class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # can't equall split among k partitions
        if sum(nums) % k != 0: return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        visited = [False] * len(nums)
        def backtrack(i, total, k):
            # have formed k partitions
            if k == 0: return True

            # subset sum = target so we can form a partition
            if total == target: return backtrack(0, 0, k - 1)

            # iterate through nums
            for j in range(i, len(nums)):
                # if element has already been visited or
                # the subset sum > target, we can skip
                if visited[j] or total + nums[j] > target: continue
                visited[j] = True
                if backtrack(j + 1, total + nums[j], k): return True
                visited[j] = False

                # PRUNING
                if total == 0: return False
            return False
        return backtrack(0, 0, k)