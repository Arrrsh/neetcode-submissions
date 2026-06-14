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
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        dummy = ListNode(next=head)
        prev_group_tail = dummy
        while prev_group_tail:
             # Check if there are k nodes remaining
            curr = prev_group_tail
            for _ in range(k):
                curr = curr.next
                if curr is None:
                    # Less than k nodes remaining, return result
                    return dummy.next
             # Save pointers for group reversal
            group_head = prev_group_tail.next
            next_group_head = curr.next
             # Disconnect current group from rest of the list
            curr.next = None
             # Reverse the current group and connect it back
             
            prev_group_tail.next = reverse(group_head)
             # After reversal, original head becomes the tail
            group_head.next = next_group_head
             # Move to the next group
            prev_group_tail = group_head
        return dummy.next