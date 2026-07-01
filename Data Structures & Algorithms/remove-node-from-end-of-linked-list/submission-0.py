# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            length += 1
            cur = cur.next
        
        first = prev = dummy

        for i in range(length - n - 1):
            first = first.next
            prev = prev.next

        first = first.next
        prev.next = first.next
        first.next = None
        return dummy.next