class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.sentinel = Node()
    
    def get(self, index: int) -> int:
        curr = self.sentinel
        idx = -1

        while curr and idx != index:
            idx += 1
            curr = curr.next

        if curr:
            return curr.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.sentinel.next)
        self.sentinel.next = new_node

    def insertTail(self, val: int) -> None:
        curr = self.sentinel
        while curr.next:
            curr = curr.next

        new_node = Node(val, None)
        curr.next = new_node
        

    def remove(self, index: int) -> bool:
        curr_idx = -1
        curr = self.sentinel

        while curr and curr_idx != (index - 1):
            curr_idx += 1
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        curr = self.sentinel.next

        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
