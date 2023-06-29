#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        b= int(num**(0.5))
        if num==b**2:
            return True 
        else:
            return False
# @lc code=end

