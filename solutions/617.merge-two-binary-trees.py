#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(t1,t2):
            if t1 and t2:
                t3=TreeNode(t1.val+t2.val)
                t3.left=merge(t1.left,t2.left)
                t3.right=merge(t1.right,t2.right)
                return t3
            elif t1 or t2:return t1 or t2
        return merge(root1,root2)
# @lc code=end

