class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        max_freq = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


        '''
        0 1 2 3
        X Y Y X     k = 2
        L
              R

        freq = {X: 2, Y: 2}
        max_freq = 2
        res = 4
        '''