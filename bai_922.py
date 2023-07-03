#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        c=[]
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c
# @lc code=end

