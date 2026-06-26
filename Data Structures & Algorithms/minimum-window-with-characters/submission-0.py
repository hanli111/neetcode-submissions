class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        res, res_len = [-1, -1], float('inf')
        l = 0
        have, need = 0, len(count_t)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float('inf') else ""


