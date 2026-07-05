# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        return dummy.next