class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val=-1):
        self.node = Node(val)
        self.tail = self.node
    
    def get(self, index: int) -> int:
        curr = self.node.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.node.next
        self.node.next = new_node
        self.node = self.node
        if not new_node.next:
            self.tail = new_node # if the list was empty

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

        # new_node = Node(val)
        # curr = self.node
        # while curr.next:
        #     curr = curr.next
        # curr.next = new_node 
        # new_node.next = None


    def remove(self, index: int) -> bool:
        i = index
        curr = self.node
        while i > 0 and curr:
            i -= 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.node.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
