#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Chuyển các số trong nums thành chuỗi và sắp xếp theo thứ tự giảm dần của số ghép được
      sorted_nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
    
    # Nếu số đầu tiên là 0 thì trả về "0", ngược lại trả về số ghép được
      return "0" if sorted_nums[0] == "0" else "".join(sorted_nums)
# @lc code=end

