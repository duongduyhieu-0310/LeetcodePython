#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        for i in accounts:
            s=0
            for j in i:
                s=s+j
            a.append(s)
        c=max(a)
        return c
# @lc code=end

