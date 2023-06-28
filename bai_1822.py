#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for i in nums:
            s*=i
        if s>0:
            return 1
        elif s==0:
            return 0
        else :
            return -1
            
# @lc code=end

