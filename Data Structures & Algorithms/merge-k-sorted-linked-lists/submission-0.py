# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
        minHeap = [h for h in lists if h]
        heapq.heapify(minHeap)
        dummy = ListNode()
        cur = dummy
        while minHeap:
            minHead = heapq.heappop(minHeap)
            if minHead.next:
                heapq.heappush(minHeap, minHead.next)
            cur.next = minHead
            cur = cur.next
        return dummy.next