#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(t,arr,st):
            if t==0:res.append(arr[:]);return
            elif t<0:return
            for i in range(st,len(candidates)):
                c=candidates[i]
                arr.append(c)
                backtrack(t-c,arr,i)
                arr.pop()
        backtrack(target,[],0)
        return res

# @lc code=end

