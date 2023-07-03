#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"

        minus = 0
        
        if num < 0:
            minus = 1
            num *= -1
        ans=''
        while num > 0:

            a = num % 7

            num -= a

            num = num//7

            ans = str(a) + ans
        
        if minus:
            ans = "-" + ans

        return ans
# @lc code=end

