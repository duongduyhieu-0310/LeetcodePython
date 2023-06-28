#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != a[i]:
                count += 1
        return count

# @lc code=end

