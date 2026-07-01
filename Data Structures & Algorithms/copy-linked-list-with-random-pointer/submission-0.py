"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # maps old nodes to deep copied nodes
        mp = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            mp[cur] = copy
            cur = cur.next
        
        # connect the deep copied nodes' pointers
        cur = head
        while cur:
            copy = mp[cur]
            copy.next = mp[cur.next]
            copy.random = mp[cur.random]
            cur = cur.next
        
        return mp[head]