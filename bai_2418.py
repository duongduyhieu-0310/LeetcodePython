#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
           
    # Kết hợp danh sách tên và chiều cao lại với nhau
    combined = list(zip(names, heights))

    # Sắp xếp danh sách kết hợp theo chiều cao giảm dần và tên tăng dần
    sorted_combined = sorted(combined, key=lambda x: (-x[1], x[0]))

    # Chuyển đổi danh sách kết quả thành danh sách các tên và trả về
    return [x[0] for x in sorted_combined]


# @lc code=end

