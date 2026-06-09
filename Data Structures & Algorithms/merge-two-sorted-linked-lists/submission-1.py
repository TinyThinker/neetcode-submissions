# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:       
        # we need to traverse both lists
        # we need to determine which one is larger than the other one
        # if one list is over we should just append the next list as the next node
        # we should keep a head node
        # and a node to track the new list which in itself is being pseudo traversed
        # as we a creating it.

        head = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        
        return head.next