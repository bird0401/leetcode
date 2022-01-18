#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=[]
        for e in nums:
            m=bisect_left(l,e)
            print(m)
            if m==len(l):l.append(e)
            else:l[m]=e
        print(l)
        return len(l)
# @lc code=end

