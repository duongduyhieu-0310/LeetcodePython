#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr=list(str(n))
        a=[]

        for i in arr:
            a.append(int(i))

        b= sum(a)
        c=1
        for j in a:
            c=c*j
        result= c-b
        return result
# @lc code=end

