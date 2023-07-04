#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in nums:
            if i<0:
              a.append(i)
            else:
              b.append(i)
        c=[]
        for j in b:
            if -j in a:
                c.append(j)
        if c==[]:
          return -1
        else: 
          return max(c)
# @lc code=end

