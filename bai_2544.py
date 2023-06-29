#
# @lc app=leetcode id=2544 lang=python3
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a=list(str(n))
        A=[]
        for i in a:
            A.append(int(i))
        b=[]
        for j in range (len(A)):
            if j%2==0:
              b.append(A[j])
            else:
              b.append(A[j]*(-1))
        return sum(b)
        
# @lc code=end

