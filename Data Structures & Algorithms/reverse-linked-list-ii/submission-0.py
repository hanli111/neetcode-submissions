# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # traverse l - 1 to get the start of reverse
        # cur is where we start to reverse
        left_prev = dummy
        cur = head
        for _ in range(left - 1):
            left_prev = cur
            cur = cur.next
        
        # traverse r - l + 1 for reverse
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # point left previous next next and next
        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next