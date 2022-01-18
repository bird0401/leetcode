#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        seen_node=set()
        current=head
        while current:
            if current in seen_node:return True
            seen_node.add(current)
            current=current.next
        return False

# s1=ListNode(3)
# s2=ListNode(2)
# s3=ListNode(0)
# s4=ListNode(-4)

# s1.next=s2
# s2.next=s3
# s3.next=s4
# S=Solution()
# print(S.hasCycle(s1))
        
# @lc code=end