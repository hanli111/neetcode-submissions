class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pv] += self.size[pu]
        else:
            self.parent[pu] = pv
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # DSU method
        dsu = DSU(len(accounts))

        # email -> index of account
        emailToAcc = {}

        # process every account and skip the names to get emails only
        for i, a in enumerate(accounts):
            for e in a[1:]:
                # connect accounts with the same emails
                if e in emailToAcc:
                    dsu.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        # index of account -> list of emails
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            # group emails by leader
            leader = dsu.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res