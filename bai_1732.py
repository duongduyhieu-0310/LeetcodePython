#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        highest=0
        for x in gain:
            curr+=x
            highest=max(curr,highest)

        return highest  
# @lc code=end

