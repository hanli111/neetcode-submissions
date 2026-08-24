class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # append in reverse order so when we pop, we get smallest
        # lexicographic airport
        adj_list = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            adj_list[u].append(v)
        
        res = []
        stk = ["JFK"]
        while stk:
            curr = stk[-1]
            if not adj_list[curr]:
                res.append(stk.pop())
            else:
                stk.append(adj_list[curr].pop())
        return res[::-1]