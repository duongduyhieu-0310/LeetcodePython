#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        a = 1   # Đại diện cho hàng đơn vị, hàng chục, hàng trăm, ...
        
        while a <= n:
            # Phân ra thành 2 phần: số từ hàng đơn vị đến hàng đang xét và số từ hàng sau nó
            b = n // (a * 10)
            c = n % (a * 10)
            
            # Số chữ số 1 xuất hiện do hàng đang xét
            count += b * a
            
            # Xét hàng hiện tại
            e = c // a
            if e == 1:
                count += c % a + 1
            elif e > 1:
                count += a
            
            # Tăng giá trị hàng lên 10 lần
            a *= 10
        
        return count
# @lc code=end

