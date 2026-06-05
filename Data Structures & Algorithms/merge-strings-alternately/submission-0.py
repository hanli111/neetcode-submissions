class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        l1, l2 = 0, 0
        res = ""

        while l1 < max(n1, n2) or l2 < max(n1, n2):
            if l1 < len(word1):
                res += word1[l1]
            if l2 < len(word2):
                res += word2[l2]
            l1 += 1
            l2 += 1
        
        return(res)