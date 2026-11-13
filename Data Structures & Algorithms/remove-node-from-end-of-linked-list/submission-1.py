# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = follower = head

        steps = n + 1
        while steps:
            if not leader:
                return head.next
            leader = leader.next
            steps -= 1

        while leader:
            follower = follower.next
            leader = leader.next

        follower.next = follower.next.next

        return head
        