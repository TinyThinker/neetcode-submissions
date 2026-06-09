# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We could do reversal but we can also do a stack
        if not l1 and not l2:
            return ListNode(0)
        
        if l1 and not l2 or l2 and not l1:
            return l1 or l2

        #Process
        num1, num2 = self.get_num(l1), self.get_num(l2)
        num_sum = str(num1 + num2)
        print(f"num1 = {num1}, num2 = {num2}")
        print(f"num_sum = {num_sum}")

        sentinel = node = ListNode(0)
        for num in num_sum:
            node.next = ListNode(int(num), node.next)
        
        return sentinel.next

    def get_num(self, head):
        curr, stack = head, []
        while curr:
            stack.append(curr.val)
            curr = curr.next

        num = 0
        index = 0
        for i in range(len(stack)):
            num += stack[i] * 10 ** index
            index += 1

        return num



        