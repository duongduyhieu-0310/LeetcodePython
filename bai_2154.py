#
# @lc app=leetcode id=2154 lang=python3
#
# [2154] Keep Multiplying Found Values by Two
#

# @lc code=start
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in nums:
            if i== original:
                original=original*2
        return original

# @lc code=end

