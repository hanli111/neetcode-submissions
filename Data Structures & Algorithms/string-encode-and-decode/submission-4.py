class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find delimiter #
            j = i

            while s[j] != "#":
                j += 1

            # get length
            length = int(s[i:j])

            # extract word
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # move pointer
            i = j + 1 + length

        return res