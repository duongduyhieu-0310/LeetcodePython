#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=matrix
        min_r = [min(x) for x in m]
        max_c = []
        for i in range(len(m[0])):
            tmp = []
            for j in range(len(m)):
                tmp.append(m[j][i])
            max_c.append(max(tmp))
        return set(min_r)&set(max_c)
# @lc code=end

