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
        current_old = head
        sentinel_new = current_new = Node(0, None, None)
        old_to_new_map = {None : None}

        while current_old:
            current_new.next = self.copy_node(current_old, old_to_new_map)
            current_new = current_new.next
            current_old = current_old.next

        current_old = head
        current_new = sentinel_new.next
        while current_old:
            current_new.random = old_to_new_map[current_old.random]
            current_old = current_old.next
            current_new = current_new.next

        return sentinel_new.next

        
    def copy_node(self, original_node, old_to_new_map):
        new_node = Node(original_node.val, original_node.next, None)
        old_to_new_map[original_node] = new_node
        return new_node


        