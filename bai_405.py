#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
          return "0"
    
        hex_digits = "0123456789abcdef"
        result = []
        
        if num < 0:
            num += 2 ** 32
        
        while num > 0:
            digit = num % 16
            result.insert(0, hex_digits[digit])
            num //= 16
        
        if num < 0:
            for i in range(len(result)):
                result[i] = hex_digits[15 - int(result[i], 16)]
        
        return "".join(result)
# @lc code=end

