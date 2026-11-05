# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        def reverse(head):
            prev = None 
            curr = head 
            while curr:
                nex = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nex 
            return prev 
        
        nhead = reverse(head)
        res = []
        stack = []
        while nhead:
            while stack and stack[-1]<=nhead.val:
                stack.pop()
            res.append(stack[-1] if stack else 0)
            stack.append(nhead.val)
            nhead = nhead.next 
        return res[::-1]