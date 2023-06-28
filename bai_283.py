#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums
        
# @lc code=end

