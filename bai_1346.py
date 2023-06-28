#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l=len(arr)
        for i in range(l):
            for j in range(l):
                if (i != j) and (arr[i]==2*arr[j]):
                    return True
        return False
# @lc code=end

