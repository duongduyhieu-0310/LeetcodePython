#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        idx = cnt = 0

        for num in nums:
            
            idx += num < target
            cnt += num == target

        return list(range(idx, idx+cnt))
# @lc code=end

