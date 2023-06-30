#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i in range(len(points)):
            x, y = points[i]
            a = (x ** 2 + y ** 2) ** 0.5
            ans.append((a, points[i]))
          # Sắp xếp các khoảng cách từ bé đến lớn

        ans.sort()  
        result = []
        for j in range(k):

            result.append(ans[j][1])

        return result     
# @lc code=end

