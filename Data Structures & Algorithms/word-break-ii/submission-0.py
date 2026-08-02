class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def backtrack(i: int, cur: List[str]):
            if i == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in wordDict:
                    cur.append(word)
                    backtrack(j + 1, cur)
                    cur.pop()
        backtrack(0, [])
        return res