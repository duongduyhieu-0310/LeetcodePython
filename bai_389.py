#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lis1 = list(s)
        lis2 = list(t)
        
        for i in lis1:
            if i in lis2:
                lis2.remove(i)
                
        return "".join(lis2)
# @lc code=end

