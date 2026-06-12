class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/")
        stk = []
        for p in path_arr:
            if p == '..':
                if stk:
                    stk.pop()
            elif p != '' and p != '.':
                stk.append(p)
        return("/" + "/".join(stk))
        

        '''
        ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        
        
        stk = ['neetcode', 'practice', '...']
        '''