#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        visited=set()
        while node is not None:
            if node in visited:return node
            else:
                visited.add(node)
                node=node.next
        return None
        
# @lc code=end

