#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)-1
        left,right=0,n
        while left<right-1:
            mid=(left+right)//2
            if nums[mid]<nums[right]:right=mid
            else:left=mid
        if nums[left]<nums[right]:return nums[left]
        else:return nums[right]
# @lc code=end

# 1 2 3 4 5
# 3 4 5 1 2
# 5 1 2 3 4