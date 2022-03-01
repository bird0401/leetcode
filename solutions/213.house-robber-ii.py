#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        def rob_simple(ns):
            n=len(ns)
            dp=[0]*(n+1)
            dp[n-1]=ns[n-1]
            for i in range(n-2,-1,-1):
                dp[i]=max(dp[i+1],dp[i+2]+ns[i])
            return dp[0]
        return max(rob_simple(nums[:-1]),rob_simple(nums[1:]))
# @lc code=end

