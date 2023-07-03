#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in nums:
            if i<pivot:
                a.append(i)
            elif i==pivot:
                b.append(i)
            else:
                c.append(i)
        d=a+b+c
        return d      

# @lc code=end

