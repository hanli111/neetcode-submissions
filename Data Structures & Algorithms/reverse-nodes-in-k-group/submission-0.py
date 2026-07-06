# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_kth_node(self, curr: Optional[ListNode], k: int):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = self.get_kth_node(group_prev, k)

            # reached the end
            if not kth_node:
                break
            
            # start reversing the kth node
            group_next = kth_node.next
            curr = group_prev.next
            prev = kth_node.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # after reversing, set up ptrs again
            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp
        
        return dummy.next