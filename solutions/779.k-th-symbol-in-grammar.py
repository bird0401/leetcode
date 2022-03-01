#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def calc(n,k):
            if n==1:return 0
            mid=2**(n-2)
            if k>mid: return 1-calc(n-1,k-mid)
            else: return calc(n-1,k)
        return calc(n,k)
# @lc code=end