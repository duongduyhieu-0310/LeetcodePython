#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1)
        b=set(nums2)
        c=a & b
        if c==set():
            return -1
        else:
            return min(c)
# @lc code=end

