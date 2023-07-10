#
# @lc app=leetcode id=2078 lang=python3
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        for i in range(len(colors)-1,0,-1):
            a=colors[i]
            b=colors[0]
            if a!=b :
               result1=i
               break
        for j in range(0,len(colors),1):
            c=colors[j]
            d=colors[len(colors)-1]
            if c!=d :
               result2=len(colors)-j-1
               break

        return max(result1,result2)
# @lc code=end

