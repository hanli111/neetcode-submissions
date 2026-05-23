class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        # check every word but the first
        for word in strs[1:]:
            while not word.startswith(prefix):
                # reset prefix to every char but the last
                prefix = prefix[:-1]
                print(prefix)
        return prefix

        '''
        sliding window


        res = ""
        b a t   
         
        
        b a g   
        

        b a n k   
        

        b a n d


        '''