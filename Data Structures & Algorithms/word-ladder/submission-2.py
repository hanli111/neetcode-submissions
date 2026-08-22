from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        # build the graph
        adj_list = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj_list[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord: return res
                for j in range(len(node)):
                    pattern = node[:j] + "*" + node[j + 1:]
                    for neigh in adj_list[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            res += 1
        return 0