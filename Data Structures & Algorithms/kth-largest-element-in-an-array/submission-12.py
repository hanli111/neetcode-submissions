class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max_heap = nums
        # for i in range(len(max_heap)):
        #     max_heap[i] = -max_heap[i]
        # heapq.heapify(max_heap)

        # for _ in range(k - 1):
        #     heapq.heappop(max_heap)

        # return -1 * max_heap[0]

        '''
        QUICKSELECT - AVERAGE CASE O(n) 
        '''
        import random
        k = len(nums) - k
        def quickselect(l, r):
            if l == r:
                return nums[l]

            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = nums[r]
            p = l

            # partition left and right subarr
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            # swap pivot and p
            nums[p], nums[r] = nums[r], nums[p]

            # recurse to the right
            if p > k:
                return quickselect(l, p - 1)
            # recurse to the left
            elif p < k:
                return quickselect(p + 1, r)
            # found the solution
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)