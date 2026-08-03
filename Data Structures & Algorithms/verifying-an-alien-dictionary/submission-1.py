class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_idx = { c : i for i, c in enumerate(order) }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                # w2 is a prefix of w1 which is not allowed
                if j == len(w2): return False

                if w1[j] != w2[j]:
                    # w2's character comes before which is not allowed
                    if char_to_idx[w2[j]] < char_to_idx[w1[j]]: return False
                    break
        return True