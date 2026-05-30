class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        '''
        [1, 2, 4, 6]
         i
            R

        res = []
        for i in range len nums
            product = 1
            r = 1
            while nums[i] != nums[r]
                product *= nums[r] -> product = 1*2*4*6
                r += 1
            res.append(product) -> res = [48]

        


        return [48, 24, 12, 8]
        '''