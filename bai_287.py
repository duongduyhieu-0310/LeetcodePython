#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=[]
        b=set()
        for i in nums:
            if i in b:
               a.append(i)
            else:
               b.add(i)
        return a[0]
# @lc code=end

