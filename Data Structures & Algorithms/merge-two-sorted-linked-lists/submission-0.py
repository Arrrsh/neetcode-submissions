# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = ListNode()
        # cur = head
        # cur1 = list1
        # cur2 = list2
        # while cur1 and cur2:
        #     if cur1.val < cur2.val:
        #         head.next = cur1
        #         cur1 = cur1.next
        #     else:
        #         head.next = cur2
        #         cur2 = cur2.next
        #     head = head.next
        # head.next = cur1 or cur2
           
        # return cur.next
        dummy = head = ListNode()
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        

            

