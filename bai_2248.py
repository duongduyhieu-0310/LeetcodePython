#
# @lc app=leetcode id=2248 lang=python3
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        res = list(res)
        res.sort()
        return res
# @lc code=end

