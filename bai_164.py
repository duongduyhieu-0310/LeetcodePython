#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=1:
            return 0
        else:
            a=[]
            for i in range(len(nums)-1):
                b=nums[i+1]-nums[i]
                a.append(b)
            return max(a)
# @lc code=end

