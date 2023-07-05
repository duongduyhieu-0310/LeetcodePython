#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = 0
        while nums != [0]*n:
            count += 1
            small = min([i for i in nums if i > 0])
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= small
        return count
        
# @lc code=end

