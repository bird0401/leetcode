#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum,maxsum=-float("inf"),-float("inf")
        for e in nums:
            currentsum=max(e,currentsum+e)
            maxsum=max(currentsum,maxsum)
        return maxsum
# @lc code=end

