#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastCheck = -1
        dupCount = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dupCount += 1 
                if dupCount > 2:
                    if lastCheck < 0:
                        lastCheck = i
                else:
                    if lastCheck >= 0:
                        nums[lastCheck] = nums[i]
                        lastCheck += 1 
            else:
                dupCount = 1 
                if lastCheck >= 0:
                    nums[lastCheck] = nums[i]
                    lastCheck += 1 
                
        if lastCheck < 0:
            return len(nums)
        else:
            return lastCheck
# @lc code=end

