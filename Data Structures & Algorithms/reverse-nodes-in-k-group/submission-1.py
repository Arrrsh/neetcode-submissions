# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        dummy = ListNode(next=head)
        prev_group_tail = dummy
        while prev_group_tail:
            curr = prev_group_tail
            for _ in range(k):
                curr = curr.next
                if curr is None:
                    return dummy.next
            group_head = prev_group_tail.next
            next_group_head = curr.next
            curr.next = None
            prev_group_tail.next = reverse(group_head)
            group_head.next = next_group_head
            prev_group_tail = group_head
        return dummy.next
            