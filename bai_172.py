#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        b = 1
        for i in range(n, 0, -1):
            b *= i
            
        a = list(str(b))
        count=0
        for i in range (len(a)-1,0,-1):
          if a[i]=="0":
            count=count+1
          else:
            break
        return count

# @lc code=end

