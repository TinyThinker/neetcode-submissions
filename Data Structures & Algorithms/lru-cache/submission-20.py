class Node:
    def __init__(self, val = 0, next = None, prev = None, key = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    def insert(self, key, val):
        new_node = Node(val, self.start.next, self.start, key)
        self.cache[key] = new_node

        self.start.next.prev = new_node
        self.start.next = new_node

    def get(self, key: int) -> int:
        cached_node = self.cache.get(key, None)
        if not cached_node:
            return -1

        prev, next = cached_node.prev, cached_node.next

        # Adjust cached surroindings
        prev.next = next
        next.prev = prev

        # Adjust start
        next = self.start.next
        self.start.next = cached_node
        next.prev = cached_node
        cached_node.prev = self.start
        cached_node.next = next       

        return cached_node.val 


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.insert(key, value)
        else:
            self.update(key, value)

        if len(self.cache) > self.capacity:
            self.delete(self.end.prev)

    def update(self, key, val):
        self.delete(self.cache[key])
        self.insert(key, val)

    def delete(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        del self.cache[node.key]





        
