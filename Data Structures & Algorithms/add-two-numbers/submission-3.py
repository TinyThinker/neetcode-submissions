# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = 0
        d2 = 0

        curr = l1
        exp = 0
        while curr:
            d1 += curr.val * (10 ** exp) 
            exp += 1
            curr = curr.next

        curr = l2
        exp = 0
        while curr:
            d2 += curr.val * (10 ** exp)
            exp += 1
            curr = curr.next

        res = str(d1 + d2)
        s_res = prev = ListNode()
        for c in res[::-1]:
            print(c)
            prev.next = ListNode(val=int(c))
            prev = prev.next

        return s_res.next


        