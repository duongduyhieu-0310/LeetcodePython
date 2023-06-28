#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)
        y=set(nums2)
        return list(x.intersection(y))
# @lc code=end

