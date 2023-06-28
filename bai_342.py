#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
          return False
    # Kiểm tra xem n có phải là số chẵn hay không
        if n & (n - 1) != 0:
          return False
    # Kiểm tra xem số bit 1 có nằm ở vị trí chẵn hay không
        if n & 0x55555555 == n:
           return True
        else:
           return False
# @lc code=end

