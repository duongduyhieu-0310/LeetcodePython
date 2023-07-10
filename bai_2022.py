#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []  # Trả về một mảng 2D trống nếu không thể tạo được

        arr_2d = []
        for i in range(m):
            row = original[i * n : (i + 1) * n]
            arr_2d.append(row)

        return arr_2d

# @lc code=end

