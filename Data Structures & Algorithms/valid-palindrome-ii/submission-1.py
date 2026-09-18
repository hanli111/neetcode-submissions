class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l + 1 : r + 1], s[l : r]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            l, r = l + 1, r - 1
            
        return True

        '''
        check s[l + 1 : r + 1] == to its reverse and
        check s[l : r] == to its reverse
        if either or is true, return true
        else false
        '''