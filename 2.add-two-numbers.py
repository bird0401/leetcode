#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def addTwoNumbers(self,l1,l2):
        head=ListNode()
        current=head
        carry=0
        while l1 or l2:
            n1=l1.val if l1 else 0
            n2=l2.val if l2 else 0
            carry, digit=divmod(carry+n1+n2,10)
            current.next=ListNode(digit)
            current=current.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry>0:current.next=ListNode(carry)
        return head.next

        
# @lc code=end

