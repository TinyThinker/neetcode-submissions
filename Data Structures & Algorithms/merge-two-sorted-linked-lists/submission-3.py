# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We will add two new nodes. One as a sentinel node
        # and one as the current node. 
        # We will continue the merging as long as there are nodes in both list1
        # and list2.
        # We will compare the heads of both list1 and list2
        # whichever is smaller will be inserted.
        # The list the merged node comes from needs to be advanced.
        sentinel = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2

        return sentinel.next


                
