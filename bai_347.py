#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Đếm tần suất xuất hiện của các phần tử trong nums
        counter = collections.Counter(nums)
    
           # Chọn ra k phần tử có tần suất cao nhất
        return [item[0] for item in counter.most_common(k)]
# @lc code=end

