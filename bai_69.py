#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        i = 1
        result = 1
        while result * result <= x:
            i += 1
            result = i

        return result - 1
# @lc code=end

