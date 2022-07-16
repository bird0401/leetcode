#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter
from re import I
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for index, character in enumerate(s):
            if c[character]==1: 
                return index
        return -1
        
# @lc code=end

