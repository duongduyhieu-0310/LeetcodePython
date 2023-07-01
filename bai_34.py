#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            res=[]
            if target not in nums:
                return [-1,-1]
            res.append(nums.index(target))
            for x in range(len(nums)-1,-1,-1):
                if(nums[x]== target ):
                    res.append(x)
                    break
            
            return res
# @lc code=end

