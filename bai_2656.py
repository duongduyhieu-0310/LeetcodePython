#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements 
#

# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=[]
        for i in range(k):
            a.append(nums[len(nums)-1]+i)
            
        return sum(a)
# @lc code=end

