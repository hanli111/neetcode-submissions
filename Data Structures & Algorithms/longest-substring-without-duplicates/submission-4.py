class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


        '''
        0 1 2 3 4 5 6 7
        a b c a b c b b
                L
                    R

        set = (a, c, b)
        res = 3

        return res
        '''