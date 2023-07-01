#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Xử lí các trường hợp đặc biệt
        if dividend == 0:  # Nếu số bị chia là 0
            return 0

        if divisor == 1:  # Nếu số chia là 1
            return dividend

        if divisor == -1:  # Nếu số chia là -1
            if dividend > -2147483648:  # Kiểm tra nếu dividend không phải là giá trị nhỏ nhất của kiểu INT32
                return -dividend  # Trả về giá trị âm của dividend

            return 2147483647  # Trường hợp dividend là giá trị nhỏ nhất của kiểu INT32 (-2^31)

        # Xác định dấu của kết quả
        sign = (dividend < 0) ^ (divisor < 0)

        # Chuyển đổi cả dividend và divisor thành giá trị dương
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0  # Biến để lưu trữ kết quả

        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1

            # Tìm divisor lớn nhất có thể trừ từ dividend
            while (temp_divisor << 1) <= dividend:
                temp_divisor <<= 1
                multiple <<= 1

            # Trừ divisor từ dividend và tăng kết quả theo multiple
            dividend -= temp_divisor
            quotient += multiple

        if sign:  # Nếu kết quả có dấu âm
            quotient = -quotient

        # Kiểm tra nếu kết quả vượt qua giới hạn của kiểu INT32
        if quotient < -2147483648 or quotient > 2147483647:
            return 2147483647

        return quotient
# @lc code=end

