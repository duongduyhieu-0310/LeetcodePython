#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # Tính số bit của num
        num_bits = num.bit_length()

        # Tạo mask
        mask = (1 << num_bits) - 1

        # Lấy phần đảo ngược của num
        complement = num ^ mask

        # Chuyển đổi kết quả sang hệ thập phân
        complement_dec = int(bin(complement)[2:], 2)

        return complement_dec
# @lc code=end

