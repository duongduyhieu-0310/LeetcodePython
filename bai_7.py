#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Chuyển số nguyên thành dạng chuỗi
        str_x = str(x)
        
        # Xác định chiều dài và vị trí bắt đầu của số trong chuỗi
        length = len(str_x)
        start = 0
        if str_x[0] == '-' or str_x[0] == '+':
            start = 1
        
        # Đảo ngược chuỗi từ vị trí start
        reversed_str = str_x[start:][::-1]
        
        # Chuyển chuỗi đảo ngược thành số nguyên
        reversed_num = int(reversed_str) if x >= 0 else -int(reversed_str)
        
        # Kiểm tra giá trị của số nguyên đảo ngược
        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0
        
        return reversed_num
# @lc code=end

