#
# @lc app=leetcode id=1619 lang=python3
#
# [1619] Mean of Array After Removing Some Elements
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        a=set(arr)
        b=list(a)

        s=(sum(b)/(len(b)))

        return s

# @lc code=end

