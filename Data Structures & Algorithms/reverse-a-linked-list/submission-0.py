# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1 , 2, 3
        # curr
        # prev
        #1.next = 2, 2.next = 3, 3.next = None
        #3.next = 2, 2.next = 1, 1.next = None
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next  = prev
            prev = curr
            curr = temp
        return prev
