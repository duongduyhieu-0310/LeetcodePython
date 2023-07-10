#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if(low & 1):
            if(high & 1):
                return int((high-low)/2 + 1);
            else:
                return int(math.ceil((high-low)/2));
        else:
            if(high & 1):
                return int(math.ceil((high-low)/2));
            else:
                return int((high-low)/2);
# @lc code=end

