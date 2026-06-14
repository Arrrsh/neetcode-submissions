# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = head
        new_curr = prev
        while curr and new_curr:
            temp = curr.next
            temp1 = new_curr.next
            curr.next = new_curr
            new_curr.next = temp
            curr = temp
            new_curr = temp1