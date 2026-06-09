# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sentinel = node = ListNode()

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None

        # Slow pointer is now the mid point.
        # No need to use fast.
        # Now we need to reverse
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt       

        # merge
        first, second = head, prev    # head = [2, 4]  - prev [8, 6]
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        
        