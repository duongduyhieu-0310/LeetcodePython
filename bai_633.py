#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            b0 = c - a**2
            b = int(b0**0.5)
            
            if b**2 == b0:
                return True
        
        return False
# @lc code=end

