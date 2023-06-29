#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(2,num+1):
            s=sum([int(a) for a in str(i)])
            if s%2==0:
                c+=1
        return c
# @lc code=end

