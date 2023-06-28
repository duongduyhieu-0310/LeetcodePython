#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ncreasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                increasing = False
            if nums[i] > nums[i-1]:
                decreasing = False
                
        return increasing or decreasing
# @lc code=end

