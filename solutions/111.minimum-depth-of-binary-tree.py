#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:return 0
            children=[node.left,node.right]
            if not any(children):return 1
            mind=float("inf")
            for c in children:
                if c:mind=min(mind,dfs(c))
            return mind+1
        return dfs(root)


# @lc code=end

