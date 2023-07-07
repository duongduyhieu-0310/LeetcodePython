#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return (s1&s2) | (s2&s3) | (s1&s3)
# @lc code=end

