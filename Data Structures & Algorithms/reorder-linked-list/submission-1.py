# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Severe first half 
        # Point to start of second half
        f_half = head
        s_half = slow.next
        slow.next = None

        # Reverse second half
        s_rev_half = ListNode()
        while s_half:
            tmp = s_rev_half.next
            s_rev_half.next = s_half
            s_half = s_half.next
            s_rev_half.next.next = tmp

        s_half = s_rev_half.next
        while s_half:
            tmp1 = f_half.next
            tmp2 = s_half.next
            f_half.next = s_half
            s_half.next = tmp1
            f_half = tmp1
            s_half = tmp2

            