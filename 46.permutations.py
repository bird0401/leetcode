#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(p):
            if p==n:output.append(nums[:]) 
            for i in range(p,n):
               nums[i],nums[p]=nums[p],nums[i]
               backtrack(p+1)
               nums[i],nums[p]=nums[p],nums[i]
        n=len(nums)
        output=[]
        backtrack(0)
        return output 

# @lc code=end

