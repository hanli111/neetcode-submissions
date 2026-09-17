class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        res = []
        curr_size, end = 0, 0
        for i, c in enumerate(s):
            curr_size += 1
            # if last_index[c] > end:
            #     end = last_index[c]
            end = max(end, last_index[c])
            if i == end:
                res.append(curr_size)
                curr_size = 0
        return res