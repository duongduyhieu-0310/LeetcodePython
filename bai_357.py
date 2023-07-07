#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans=1
        for i in xrange(1,n+1):
            term=9
            for i in xrange(1,i):
                term*=10-i
            ans+=term
        return ans
# @lc code=end

