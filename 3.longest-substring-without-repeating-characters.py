#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right,res=0,0,0
        contain_str=set()
        while True:
            while right<len(s) and s[right] not in contain_str:
               contain_str.add(s[right])
               right+=1
            res=max(res,len(contain_str))
            if right==len(s):break 
            while s[right] in contain_str:
                contain_str.discard(s[left])
                left+=1
        return res
# @lc code=end

