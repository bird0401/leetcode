#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        current=head
        node=ListNode()
        first_node=node
        ds=set()
        while current:
            if current.next and current.val==current.next.val:ds.add(current.val)
            if current.val not in ds:
                node.next=ListNode(current.val);node=node.next
            current=current.next
        return first_node.next

# @lc code=end

