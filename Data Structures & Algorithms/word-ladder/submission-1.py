from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        # build the graph
        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neigh in graph[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
            res += 1
        return 0