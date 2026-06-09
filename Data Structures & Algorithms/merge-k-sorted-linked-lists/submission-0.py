# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minQueue = []

        for lst in lists:
            if lst:
                heapq.heappush(minQueue, NodeWrapper(lst))

        sentinel = node = ListNode(0)
        while minQueue:
            min_node = (heapq.heappop(minQueue)).node
            node.next = min_node
            node = node.next

            if min_node.next:
                heapq.heappush(minQueue, NodeWrapper(min_node.next))

        return sentinel.next






        