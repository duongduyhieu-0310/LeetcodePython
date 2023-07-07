#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        b=set(candyType)
        l=len(b)
        n=len(candyType)/2
        if l>=n:
            return n
        else:
            return l
        
        
# @lc code=end

