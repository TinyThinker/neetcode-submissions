# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s_res = res_prev = ListNode()
        curr1 = l1
        curr2 = l2

        carry = 0
        while curr1 and curr2:
            res_prev.next = ListNode(val=curr1.val + curr2.val)
            res_prev = res_prev.next

            curr1 = curr1.next
            curr2 = curr2.next

        if curr1 or curr2:
            res_prev.next = curr1 if curr1 is not None else curr2

        curr = s_res.next
        prev = None
        carry = 0
        while curr:
            curr_total = curr.val + carry
            curr.val = curr_total % 10
            carry = curr_total // 10
            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(1)
            

        return s_res.next
        

        