#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[0]*(n+1)
        min_v,res=10**8,-1
        for i in range(n):
            min_v=min(min_v,prices[i])
            res=max(res,prices[i]-min_v)
        return res
# @lc code=end

