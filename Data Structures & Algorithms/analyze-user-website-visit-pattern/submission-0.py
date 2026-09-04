class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list)
        for _, user, site in sorted(zip(timestamp, username, website)):
            visits[user].append(site)
        
        count = defaultdict(int)
        for v in visits.values():
            for pattern in set(combinations(v, 3)):
                count[pattern] += 1
        
        return list(min(count, key=lambda p: (-count[p], p)))