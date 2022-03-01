#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for i in range(2**n):
            temp=[]
            for j in range(n):
                if 1&(i>>j):temp.append(nums[j])
            res.append(temp)
        return res
        
# @lc code=end

