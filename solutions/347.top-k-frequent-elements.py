#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        return heapq.nlargest(k,counter.keys(),key=counter.get)
        # return [e[0] for e in sorted(counter.items(),key=lambda t:t[1],reverse=True)[:k]]
# @lc code=end

