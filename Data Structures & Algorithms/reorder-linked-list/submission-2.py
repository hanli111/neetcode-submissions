# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        '''
        2 -> 4 -> 6 -> 8 -> 10
        return 2 -> 10 -> 4 -> 8 -> 6

        reverse second half and disconnect linked list
        2 -> 4 -> 6     prev <- 10 <- 8
                  sl                  pr
                                              f
                                         tmp
                                         sec
                       

        2 -> 4 -> 6    10 <- 8
             f               s
                  t1              t2

        2 -> 10 -> 4 -> 8 -> 6
        '''