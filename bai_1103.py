#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
            # Khởi tạo danh sách kết quả ban đầu
    ans = [0] * num_people
    i = 0
    while candies > 0:
        # Phân phát số kẹo tối đa trong lượt lặp này
        ans[i % num_people] += min(candies, i + 1)
        candies -= i + 1
        i += 1
    return ans

# @lc code=end

