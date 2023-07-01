#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))  # Sắp xếp mảng duy nhất và loại bỏ các phần tử trùng lặp
        
        rank_dict = {}  # Tạo một từ điển để lưu trữ thứ hạng của từng giá trị

        for i, num in enumerate(sorted_arr):
            rank_dict[num] = i + 1  # Lưu trữ thứ hạng tương ứng với giá trị

        ranks = []  # Danh sách để lưu trữ kết quả cuối cùng

        for num in arr:
            ranks.append(rank_dict[num])  # Thêm thứ hạng của giá trị vào danh sách kết quả

        return ranks
# @lc code=end

