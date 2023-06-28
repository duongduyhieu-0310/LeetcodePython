#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return max(nums[0] * nums[1] * nums[n - 1], nums[n-3] * nums[n - 2] * nums[n-1])
# @lc code=end

