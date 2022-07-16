#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
# the basic idea is that the number subtracted between accumurate sums is the sum of subarray
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, sum = 0, 0
        d = {0:1}
        for num in nums:
            sum += num
            if  sum-k  in  d:
                ans = ans + d[sum-k]
            d[sum] = d.get(sum, 0) + 1
        return ans
# @lc code=end

