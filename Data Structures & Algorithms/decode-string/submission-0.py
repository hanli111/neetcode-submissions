class Solution:
    def decodeString(self, s: str) -> str:
        str_stk = []
        k_stk = []
        k = 0
        cur = ""

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                str_stk.append(cur)
                k_stk.append(k)
                cur, k = "", 0
            elif c == "]":
                tmp = cur
                cur, num = str_stk.pop(), k_stk.pop()
                cur += tmp * num
            else:
                cur += c
        return cur


        '''

        2 [ a 3 [ b ] ] c
          i

        k = 2

        str_stk = []
        k_stk = []

        iterate through
            if number:
                k = k * 10 + int()
            elif [:
                str_stk.append(c)
                k_stk.append(k)
                cur, k = "", 0
            elif ]:
                tmp = cur
                cur, num = str_stk.pop(), k_stk.pop()
                cur += tmp * num
            else:
                cur += c
        '''