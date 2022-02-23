#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if not n:return 0
        dp=[0]*(n+1)
        dp[n-1],dp[n]=nums[n-1],0
        for i in range(n-2,-1,-1):
            dp[i]=max(dp[i+2]+nums[i],dp[i+1])
        return dp[0]

# @lc code=end
