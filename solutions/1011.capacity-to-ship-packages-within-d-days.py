#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def f(min_weight):
            sum,days_cuml=0,0
            for w in weights:
                if sum+w>min_weight:
                    days_cuml+=1
                    sum=0
                sum+=w
            if sum>0:days_cuml+=1
            return days_cuml
        left,right=max(weights),10**8
        while right-left>1:
            mid=(right+left)//2
            print(f"{left},{mid},{right}")
            if f(mid)>days:left=mid
            else:right=mid
        if f(left)<=days: return left
        return right

# @lc code=end

