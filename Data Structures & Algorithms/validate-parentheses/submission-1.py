class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close_mapping = {'}' : '{', ')' : '(', ']' : '['}

        # check every character in the string
        for c in s:
            # if that character is in the map, that means there
            # is a match
            if c in close_mapping:
                # check if the stack is not empty AND
                # there is a valid opening bracket to match map
                if stk and stk[-1] == close_mapping[c]:
                    # can pop this pair out
                    stk.pop()
                else:
                    return False
            # otherwise no match yet, so append character to the
            # stack
            else:
                stk.append(c)
        
        # can only return true if the stk is empty else false
        return True if not stk else False