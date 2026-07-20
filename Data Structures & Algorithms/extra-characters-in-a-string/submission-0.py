class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_words(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.add_words(word)
        
        dp = {len(s) : 0}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.end_of_word:
                    res = min(res, dfs(j + 1))
            
            dp[i] = res
            return res
        return dfs(0)