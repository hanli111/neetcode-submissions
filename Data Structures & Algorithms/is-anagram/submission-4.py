class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        map_s = Counter(s)
        map_t = Counter(t)

        return map_s == map_t
            
        '''
        map of each letter's occurrence

        {"r": 2, ...}
        '''