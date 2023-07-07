#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=[]
        
        for i in arr1:
            if i not in arr2:
                a.append(i)
        a.sort()
        ans=[]
        for  i in arr2:
            for j in arr1:
                if i==j:
                    ans.append(i)
        return  ans+a

# @lc code=end

