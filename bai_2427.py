#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        dem=0
        for i in range(1,(min(a,b)+1)):
            if (a%i==0)and(b%i==0):
                dem=dem+1


        return dem
# @lc code=end

