#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        a=set()

        for i in range(len(nums)-1):
            b=nums[i]+nums[i+1]
            if b in a:

                return True 
            else: 
                a.add(b)
        return False
# @lc code=end

