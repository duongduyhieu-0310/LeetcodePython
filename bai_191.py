#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]  # Chuyển số nguyên thành chuỗi nhị phân
        count = 0
        for i in b:
            if i == '1':
                count += 1
        return count
# @lc code=end

