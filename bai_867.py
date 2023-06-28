#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        A=len(matrix[0])
        x=len(matrix)
        return [ [ matrix[j][i] for j in range(x)]  for i in range(A)]
# @lc code=end

