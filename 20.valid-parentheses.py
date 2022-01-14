#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        mapping={")":"(","]":"[","}":"{"}
        stack=[]
        for e in s:
            if e in mapping:
                lasts=stack.pop() if stack else "#"
                if mapping[e]!=lasts:return False
            else:
                stack.append(e)
        return not stack
# @lc code=end

