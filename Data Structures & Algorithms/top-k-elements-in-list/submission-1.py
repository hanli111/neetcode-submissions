class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = Counter(nums)

        for i in range(k):
            key = max(counts, key=counts.get)
            res.append(key)
            del counts[key]
        return res


        '''
        [1, 2, 2, 3, 3, 3]

        {1: 1, 2: 2, 3: 3}

        get a dictionary of counts of each number
        iterate k times through dictionary
            append max value's key
            pop the key value pair
        return res
        '''