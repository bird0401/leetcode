#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def in_order(left,right):
            if left>right:return None
            mid=(left+right)//2
            root=TreeNode(nums[mid],in_order(left,mid-1),in_order(mid+1,right))
            return root
        return in_order(0,len(nums)-1)
# @lc code=end

