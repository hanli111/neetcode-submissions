class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # in place heap sort
        def heapify(n, i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            # check left child
            if left < n and nums[left] > nums[largest]:
                largest = left
            # check right child
            if right < n and nums[right] > nums[largest]:
                largest = right
            
            # otherwise keep swapping
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)
        
        n = len(nums)

        # build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # extract elements one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # move max to end
            heapify(i, 0)  # restore heap

        return nums

        '''
        [1, 3, 2, 10, 5]
            i
               n

        while i < n, where n = len(nums) - 1
            check if nums[i] > nums[n]
                swap: nums[i], nums[n] = nums[n], nums[i]
                n -= 1
                
            else
                i += 1
        '''