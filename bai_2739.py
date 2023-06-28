#
# @lc app=leetcode id=2739 lang=python3
#
# [2739] Total Distance Traveled
#

# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        i = 0
        while i < mainTank:
            i += 1
            if (additionalTank != 0) and (i % 5 == 0):
                additionalTank -= 1
                result += 10
                mainTank += 1
            else:
                result += 10
        return result
# @lc code=end

