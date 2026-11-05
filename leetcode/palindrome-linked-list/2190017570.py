# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def reverse(head):
            prev = None 
            curr = head 
            while curr:
                nex = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nex 
            return prev 
        
        temp = head
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        middle = slow 
        rmiddle = reverse(middle)
        while temp and rmiddle:
            if temp.val!=rmiddle.val:
                return False 
            temp = temp.next 
            rmiddle = rmiddle.next 
        return True