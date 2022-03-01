#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while right-left>1:
            mid=(left+right)//2
            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:right=mid
                else:left=mid
            else:
                if nums[mid]<=target<=nums[right]:left=mid
                else:right=mid
        if nums[left]==target:return left
        elif nums[right]==target:return right
        return -1

# @lc code=end

# 0 1 2 3 4
# 2 3 4 0 1
# 4 0 1 2 3

# 0 1 2 
# 1 2 0 
# 2 0 1

# 4,5,6,7,0,1,2
