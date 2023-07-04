#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a=[abs(i) for i in nums]
        b=[]
        for j in nums:
            if abs(j)==min(a):
                b.append(j)
        return max(b)
# @lc code=end

