#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        mini = min(nums)
        return max(0, maxi-k-mini-k)
# @lc code=end

