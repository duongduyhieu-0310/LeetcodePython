#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums1=int(num1)
        nums2=int(num2)
        num= nums1*nums2
        nums=str(num)
        return nums
# @lc code=end

