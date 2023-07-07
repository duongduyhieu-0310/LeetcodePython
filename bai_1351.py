#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid :
            for j in i :
                if j<0 :
                    count+=1
        return count
# @lc code=end

