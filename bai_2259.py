#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxRes= 0
        for i in range(len(number)):
            if number[i]==digit:
                maxRes= max(maxRes, int(number[:i]+ number[i+1:]))
        return str(maxRes)

# @lc code=end

