#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Loại bỏ khoảng trắng đầu và cuối chuỗi
        s = s.strip()
        
        # Tìm vị trí của ký tự khoảng trắng cuối cùng
        last_space_index = s.rfind(' ')
        
        # Nếu không tìm thấy khoảng trắng, trả về độ dài toàn bộ chuỗi
        if last_space_index == -1:
            return len(s)
        
        # Lấy độ dài của từ cuối cùng
        return len(s[last_space_index+1:])

# @lc code=end

