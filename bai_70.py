#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        k1=0
        k2=1
        while n>0:
            k1,k2=k2,k1+k2
            n-=1

        return k2
# @lc code=end

