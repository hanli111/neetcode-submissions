class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # marks beginning of sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

        '''
        set = (100, 4, 200, 1, 3, 2)
        longest = 0
        num = 100

        if num - 1 not in set 
        (this mean it's the beginning of a sequence)
            length = 1
            while num + length is in the set
                length += 1
                longest = max(longest, length)
        return longest

        1-1 = 0 not in set
        length = 1
        while 1 + 1 = 2 is in the set
            length = 2
            longest = max(0, 2) = 2
        while 1 + 2 = 3 is in the set
            length = 3
            longest = max(2, 3) = 3
        while 1 + 3 = 4 is in the set
            length = 4
            longest = max(3, 4) = 4
        while 1 + 4 = 5 is not in the set
            exit
        '''