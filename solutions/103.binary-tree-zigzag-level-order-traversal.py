#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node=node_queue.popleft()
            if curr_node:
                if is_order_left: level_list.append(curr_node.val)
                else: level_list.appendleft(curr_node.val)
                if curr_node.left: node_queue.append(curr_node.left)
                if curr_node.right: node_queue.append(curr_node.right)
            else:
                ret.append(level_list)
                if len(node_queue) > 0: node_queue.append(None)

                level_list=deque()
                is_order_left = not is_order_left
                
        return ret

# @lc code=end
