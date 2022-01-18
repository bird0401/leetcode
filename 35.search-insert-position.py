#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)
        while right-left>1:
            mid=(left+right)//2
            # print(f"{left},{mid},{right}")
            if nums[mid]>target:right=mid
            else:left=mid
        if nums[left]>=target:return left
        else:return left+1
# @lc code=end



