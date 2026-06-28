# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty linked list and single element
        if not head:
            return None
        if not head.next:
            return head
        
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        '''
        none <- 0 <- 1 <- 2 <- 3 
                h
                               c
                                   n
                            p
        '''
        