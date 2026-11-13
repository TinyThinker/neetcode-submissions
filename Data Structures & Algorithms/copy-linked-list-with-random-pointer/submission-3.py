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
        s_new = new_prev = Node(-1000)
        curr = head
        random_map = {None:None}
        while curr:
            # Copy
            new_prev.next = Node(x=curr.val, random=curr.random)
            new_prev = new_prev.next

            random_map[curr] = new_prev
        
            # Advance current
            curr = curr.next

        new_curr= s_new.next
        while new_curr:
            new_curr.random = random_map[new_curr.random]
            new_curr = new_curr.next
        return s_new.next
        

        