class Node:
    def __init__(self, key: int, value: int, prev: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int): 
        self.capacity = capacity

        self.cache = {}

        self.s_head, self.s_tail = Node(-1, 0), Node(-1, 0)
        self.s_head.prev, self.s_head.next = None, self.s_tail
        self.s_tail.prev, self.s_tail.next = self.s_head, None

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return - 1

        self.remove_node(node.key)
        self.insert(node.key, node.value)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            self.remove_node(key)
        self.insert(key, value)
        

    def remove_node(self, key):
        node = self.cache.get(key, None)
        if node:
            del self.cache[key]
            node.prev.next, node.next.prev = node.next, node.prev

    def insert(self, key, value):
        node = Node(key, value, self.s_tail.prev, self.s_tail)
        self.cache[key] = node
        self.s_tail.prev.next = node
        self.s_tail.prev = node

        if len(self.cache) > self.capacity:
            self.remove_node(self.s_head.next.key)


             

        
        
