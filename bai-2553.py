#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            b=list(str(i))
            for j in b:
                a.append(int(j))
        a.sort
        return a        
# @lc code=end

