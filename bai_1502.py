#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
         n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        diff = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i - 1] != diff:
                return False
        
        return True

# @lc code=end

