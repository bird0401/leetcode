#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for email in emails:
            local,domain=email.split("@")
            if "+" in local:local=local[:local.index("+")]
            local=local.replace(".","")
            res.add(local+"@"+domain)
        set_email=set(res)
        return len(set_email)


# @lc code=end
