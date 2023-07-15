#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        l1=[]
        for i in nums:
            if(nums.count(i)==1):
                l.append(i)
            else:
                l1.append(i)
        return l
      
# @lc code=end

