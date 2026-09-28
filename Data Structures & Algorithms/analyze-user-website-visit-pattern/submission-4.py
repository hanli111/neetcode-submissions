from collections import defaultdict, Counter
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visited = sorted(zip(timestamp, username, website))

        by_user = defaultdict(list)
        for _, user, site in visited:
            by_user[user].append(site)
        
        score = Counter()
        for sites in by_user.values():
            score.update(set(combinations(sites, 3)))
        
        best = min(score, key=lambda p: (-score[p], p))
        return list(best)