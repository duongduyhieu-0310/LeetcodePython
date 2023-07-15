#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        # Đếm tần suất xuất hiện của các ký tự trong chuỗi s
        counter = Counter(s)
        
        # Sắp xếp các ký tự theo thứ tự giảm dần của tần suất xuất hiện
        sorted_chars = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
        
        # Tạo chuỗi kết quả bằng cách lặp qua các ký tự đã sắp xếp và nhân chúng với tần suất tương ứng
        result = ""
        for char in sorted_chars:
            result += char * counter[char]
        
        return result
# @lc code=end

