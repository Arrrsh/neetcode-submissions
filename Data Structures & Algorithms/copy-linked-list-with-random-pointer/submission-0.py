"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {}
        dummy = Node(0)
        tail = dummy
        cur = head
        while cur:
            new_node = Node(cur.val)
            tail.next = new_node
            tail = tail.next
            original_to_copy[cur] = new_node
            cur = cur.next
        
        cur = head
        while cur:
            if cur.random:
               original_to_copy[cur].random = original_to_copy[cur.random]
            else:
                original_to_copy[cur].random = None
            cur = cur.next
        return dummy.next
