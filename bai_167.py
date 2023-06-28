#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers)-1
        while True:
            s = numbers[p1] + numbers[p2]
            if s==target:
                break
            elif s > target:
                p2 -= 1
            else:
                p1 += 1
        return [p1+1, p2+1]
# @lc code=end

