#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_ = 0
        if num <= 1:
            return False
        if num > 1:
            for i in range(1, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    if i != 1:
                        sum_ += i + num / i
                    else:
                        sum_ += 1
            if sum_ == num:
                return True
            else:
                return False

# @lc code=end

