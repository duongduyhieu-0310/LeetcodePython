#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        s=set()
        for i in nums:
            if i in s :
                a.append(i)
            else:
                s.add(i)
        return a
        
# @lc code=end

